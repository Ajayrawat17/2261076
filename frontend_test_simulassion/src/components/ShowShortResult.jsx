const ShowShortResult = ({ data }) => {
  if (!data) return null;
  return (
    <div>
      <h4>Short URL Created</h4>
      <p>
        <a href={data.shortLink} target="_blank" rel="noreferrer">
          {data.shortLink}
        </a>
      </p>
      <small>Expires at: {new Date(data.expiry).toLocaleString()}</small>
    </div>
  );
};

export default ShowShortResult;
