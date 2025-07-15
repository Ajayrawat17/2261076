from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from .models import ShortURL
from django.utils import timezone
from nanoid import generate
from django.http import HttpResponseRedirect

@api_view(['POST'])
def create_short_url(request):
    data = request.data
    url = data.get('url')
    validity = int(data.get('validity', 30))
    shortcode = data.get('shortcode') or generate(size=6)

    if ShortURL.objects.filter(shortcode=shortcode).exists():
        return Response({'error': 'Shortcode already exists'}, status=409)

    expiry = timezone.now() + timezone.timedelta(minutes=validity)

    short = ShortURL.objects.create(
        url=url,
        shortcode=shortcode,
        expiry=expiry,
        clicks=[]
    )

    return Response({
        'shortLink': f"http://localhost:8000/shorturls/go/{shortcode}",
        'expiry': expiry.isoformat()
    })


@api_view(['GET'])
def get_stats(request, shortcode):
    try:
        short = ShortURL.objects.get(shortcode=shortcode)
    except ShortURL.DoesNotExist:
        return Response({'error': 'Not found'}, status=404)

    return Response({
        'url': short.url,
        'created_at': short.created_at,
        'expiry': short.expiry,
        'total_clicks': len(short.clicks),
        'clicks': short.clicks
    })


@api_view(['GET'])
@permission_classes([AllowAny])  # Public redirect
def redirect_url(request, shortcode):
    try:
        short = ShortURL.objects.get(shortcode=shortcode)
    except ShortURL.DoesNotExist:
        return Response({'error': 'Short URL not found'}, status=404)

    if short.expiry < timezone.now():
        return Response({'error': 'Link expired'}, status=410)

    short.clicks.append({
        'timestamp': timezone.now().isoformat(),
        'referrer': request.META.get('HTTP_REFERER', 'unknown'),
        'ip': request.META.get('REMOTE_ADDR', '')
    })
    short.save()

    return HttpResponseRedirect(short.url)
