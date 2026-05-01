/**
 * Thin API client for the Flask backend.
 * All requests go to /api/* which is:
 *   - proxied to Flask by Vite during `npm run dev`
 *   - routed to Flask by Nginx in production (see nginx.conf /api/ block)
 */

const BASE = '/api';

function authHeaders() {
  const token = localStorage.getItem('access_token');
  return token ? { Authorization: `Bearer ${token}` } : {};
}

async function request(method, path, body) {
  const opts = {
    method,
    headers: {
      'Content-Type': 'application/json',
      ...authHeaders()
    }
  };
  if (body !== undefined) opts.body = JSON.stringify(body);

  const res = await fetch(`${BASE}${path}`, opts);
  const data = await res.json().catch(() => ({}));

  if (!res.ok) {
    throw Object.assign(new Error(data.msg || 'Request failed'), { status: res.status, data });
  }
  return data;
}

// ── Auth ──────────────────────────────────────────────────────────────────────
export const auth = {
  register: (payload) => request('POST', '/register', payload),
  login:    (payload) => request('POST', '/login',    payload),
};

// ── Current user ──────────────────────────────────────────────────────────────
export const me = {
  get:    ()        => request('GET',  '/me'),
  update: (payload) => request('PUT',  '/me', payload),
};

// ── Posts ─────────────────────────────────────────────────────────────────────
export const posts = {
  list:   (category) => request('GET',    `/posts${category && category !== 'All' ? `?category=${encodeURIComponent(category)}` : ''}`),
  get:    (id)       => request('GET',    `/posts/${id}`),
  create: (payload)  => request('POST',   '/posts',    payload),
  update: (id, payload) => request('PUT', `/posts/${id}`, payload),
  remove: (id)       => request('DELETE', `/posts/${id}`),
  mine:   ()         => request('GET',    '/my-posts'),
};

// ── Admin ─────────────────────────────────────────────────────────────────────
export const admin = {
  users:   () => request('GET', '/admin/users'),
  pending: () => request('GET', '/admin/posts/pending'),
};
