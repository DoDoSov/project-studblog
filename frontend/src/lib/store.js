import { writable, derived } from 'svelte/store';

function createAuthStore() {
  const initialToken = localStorage.getItem('access_token') || null;
  let initialUser = null;
  
  try {
    const savedUser = localStorage.getItem('user');
    initialUser = savedUser ? JSON.parse(savedUser) : null;
  } catch (e) {
    console.error("Failed to parse initial user", e);
  }

  const { subscribe, set, update } = writable({
    token: initialToken,
    user: initialUser,
    isLoggedIn: !!initialToken
  });

  return {
    subscribe,

    setSession(token, user) {
      localStorage.setItem('access_token', token);
      localStorage.setItem('user', JSON.stringify(user));
      set({ 
        token, 
        user, 
        isLoggedIn: true 
      });
    },

    // Useful for when the user updates their profile (including GitHub repo)
    updateUser(user) {
      localStorage.setItem('user', JSON.stringify(user));
      update(s => ({ ...s, user }));
    },

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

export const authStore = createAuthStore();
export const isLoggedIn = derived(authStore, ($auth) => $auth.isLoggedIn);
export const user = derived(authStore, ($auth) => $auth.user);