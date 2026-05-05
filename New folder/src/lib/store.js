/**
 * Svelte 5 reactive auth store.
 * Persists the JWT and user object in localStorage so the session
 * survives page reloads.
 */

function createAuthStore() {
  // Hydrate from localStorage on first load
  let _token = $state(localStorage.getItem('access_token') ?? null);
  let _user  = $state(JSON.parse(localStorage.getItem('user') ?? 'null'));

  return {
    get token() { return _token; },
    get user()  { return _user;  },
    get isLoggedIn() { return !!_token; },

    setSession(token, user) {
      _token = token;
      _user  = user;
      localStorage.setItem('access_token', token);
      localStorage.setItem('user', JSON.stringify(user));
    },

    clearSession() {
      _token = null;
      _user  = null;
      localStorage.removeItem('access_token');
      localStorage.removeItem('user');
    }
  };
}

export const authStore = createAuthStore();
