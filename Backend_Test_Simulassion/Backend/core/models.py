from djongo import models

class ShortURL(models.Model):
    url = models.URLField()
    shortcode = models.CharField(max_length=10, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    expiry = models.DateTimeField()
    clicks = models.JSONField(default=list, blank=True)

    def add_click(self, ip, referrer=""):
        from datetime import datetime
        click_data = {
            'timestamp': datetime.now().isoformat(),
            'ip': ip,
            'referrer': referrer
        }
        self.clicks.append(click_data)
        self.save()

    def __str__(self):
        return f"{self.shortcode} → {self.url}"