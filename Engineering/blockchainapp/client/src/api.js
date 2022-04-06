export function getAccounts() {
  return fetch('https://api.helium.io/v1/accounts')
    .then(data => data.json())
}

const requestOptions = (method, json) => ({
  method,
  headers: {
    'Content-Type': json === undefined ? undefined : 'application/json',
  },
  body: json === undefined ? undefined : JSON.stringify(json),
});

export const apiURL = (url) => new URL(url, process.env.REACT_APP_BASE_URL);

const checkFetch = async (url, options) => await fetch(apiURL(url), options);

export const get = async (url) =>
  await checkFetch(url, requestOptions('GET', undefined));
export const post = async (url, json) =>
  await checkFetch(url, requestOptions('POST', json));

export const fetchData = async (url, setFn) => {
  const resp = await get(url);
  if (resp.ok) {
    setFn(await resp.json());
  }
  return resp.ok;
};

export const postData = async (url, setFn) => {
  const resp = await post(url);
  if (resp.ok) {
    setFn(await resp.json());
  }
  return resp.ok;
};