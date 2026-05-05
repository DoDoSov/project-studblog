import { writable, derived } from 'svelte/store';

function createAuthStore() {
  // 1. Initialize data from localStorage (Hydration)
  // We use 'access_token' to match your Flask backend's new key name
  const initialToken = localStorage.getItem('access_token') || null;
  const initialUser = JSON.parse(localStorage.getItem('user') || 'null');

  // 2. Create the internal writable store
  // We include isLoggedIn directly in the object so $authStore.isLoggedIn works
  const { subscribe, set, update } = writable({
    token: initialToken,
    user: initialUser,
    isLoggedIn: !!initialToken
  });

  return {
    subscribe, // Makes the store "subscribable" in components via $authStore

    /**
     * Updates the store and persists to localStorage
     * @param {string} token - The JWT access token
     * @param {object} user - The user object from Flask
     */
    setSession(token, user) {
      localStorage.setItem('access_token', token);
      localStorage.setItem('user', JSON.stringify(user));
      set({ 
        token, 
        user, 
        isLoggedIn: true 
      });
    },

    /**
     * Clears store and localStorage on logout
     */
    clearSession() {
      localStorage.removeItem('access_token');
      localStorage.removeItem('user');
      set({ 
        token: null, 
        user: null, 
        isLoggedIn: false 
      });
    }
  };
}

// The main store instance
export const authStore = createAuthStore();

/**
 * Derived store for login status (Optional)
 * Usage: import { isLoggedIn } from './store.js'; then use $isLoggedIn
 */
export const isLoggedIn = derived(authStore, ($auth) => $auth.isLoggedIn);

/**
 * Derived store for user data (Optional)
 * Usage: import { user } from './store.js'; then use $user
 */
export const user = derived(authStore, ($auth) => $auth.user);