/**
 * Thin API client for the Flask backend.
 */

const BASE = '/api';

function authHeaders() {
  const token = localStorage.getItem('access_token');
  return token ? { Authorization: `Bearer ${token}` } : {};
}

async function request(method, path, body) {
  const controller = new AbortController();
  const id = setTimeout(() => controller.abort(), 8000); // 8s Timeout to prevent infinite loading

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
    clearTimeout(id);

    const data = await res.json().catch(() => ({}));

    if (!res.ok) {
      throw Object.assign(new Error(data.msg || 'Request failed'), { status: res.status, data });
    }
    return data;
  } catch (err) {
    if (err.name === 'AbortError') throw new Error('Gateway Timeout: Backend not responding');
    throw err;
  }
}

export const auth = {
  register: (payload) => request('POST', '/register', payload),
  login:    (payload) => request('POST', '/login',    payload),
};

export const me = {
  get:    ()        => request('GET',  '/me'),
  update: (payload) => request('PUT',  '/me', payload),
};

export const posts = {
  get:    (id)       => request('GET',    `/posts/${id}`),
  create: (payload)  => request('POST',   '/posts',    payload),
  update: (id, payload) => request('PUT', `/posts/${id}`, payload),
  remove: (id)       => request('DELETE', `/posts/${id}`),
  mine:   ()         => request('GET',    '/my-posts'),
  // Enhanced list to ensure we get enough posts for all sections
  list: (category, limit = 50) => {
    let query = `?limit=${limit}`;
    if (category && category !== 'All') {
      query += `&category=${encodeURIComponent(category)}`;
    }
    return request('GET', `/posts${query}`);
  },
};

export const admin = {
  users:   () => request('GET', '/admin/users'),
  pending: () => request('GET', '/admin/posts/pending'),
};