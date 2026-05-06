const BASE = '/api';

const ID_KEYS = new Set(['id', 'user_id', 'post_id', 'author_id']);

function bigIntReviver(key, value) {
  if (ID_KEYS.has(key) && typeof value === 'number' && !Number.isSafeInteger(value)) {
    // Rarely triggers after Layer 1, but kept as a hard backstop
    return value.toString();
  }
  return value;
}

function safeParseJSON(text) {
  const fixed = text.replace(
    /("(?:id|user_id|post_id|author_id)"\s*:\s*)(\d{16,})/g,
    (_, key, num) => `${key}"${num}"`
  );
  return JSON.parse(fixed, bigIntReviver);
}

function authHeaders() {
  const token = localStorage.getItem('access_token');
  return token ? { Authorization: `Bearer ${token}` } : {};
}

async function request(method, path, body) {
  const controller = new AbortController();
  const timeoutId = setTimeout(() => controller.abort(), 8000);

  const opts = {
    method,
    signal: controller.signal,
    headers: {
      'Content-Type': 'application/json',
      ...authHeaders()
    }
  };

  if (body !== undefined) opts.body = JSON.stringify(body);

  try {
    const res = await fetch(`${BASE}${path}`, opts);
    clearTimeout(timeoutId);

    if (res.status === 204) return null;

    const text = await res.text();

    // Robust parsing: only parse if there is actually content
    let data = {};
    if (text && text.trim()) {
      try {
        data = safeParseJSON(text);
      } catch (e) {
        console.error('JSON Parse Error:', text);
        throw new Error('Received invalid response from server.');
      }
    }

    if (!res.ok) {
      if (res.status === 401) {
        localStorage.removeItem('access_token');
        window.location.href = '/#/login';
      }
      const error = new Error(data.msg || data.error || `Error ${res.status}`);
      throw Object.assign(error, { status: res.status, data });
    }

    return data;
  } catch (err) {
    if (err.name === 'AbortError') throw new Error('Backend timeout.');
    throw err;
  }
}

export const auth = {
  register: (payload) => request('POST', '/register', payload),
  login:    (payload) => request('POST', '/login',    payload),
};

export const me = {
  get:    ()        => request('GET', '/me'),
  update: (payload) => request('PUT', '/me', payload),
};

export const posts = {
  get:    (id)          => request('GET',    `/posts/${String(id)}`),
  create: (payload)     => request('POST',   '/posts', payload),
  update: (id, payload) => request('PUT',    `/posts/${String(id)}`, payload),
  remove: (id)          => request('DELETE', `/posts/${String(id)}`),
  mine:   ()            => request('GET',    '/my-posts'),

  list: (category, limit = 50, search = '') => {
    const params = new URLSearchParams({ limit });
    if (category && category !== 'All') params.append('category', category);
    if (search) params.append('search', search);
    return request('GET', `/posts?${params.toString()}`);
  },
};

export const admin = {
  users:    () => request('GET', '/admin/users'),
  pending:  () => request('GET', '/admin/posts/pending'),
  allPosts: () => request('GET', '/admin/posts/all'),
};

export const info = {
  about:    () => request('GET', '/about-static'),
  branding: () => request('GET', '/branding'),
};