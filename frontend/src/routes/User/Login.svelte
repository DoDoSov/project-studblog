<script>
  import { auth } from '../../lib/api.js';
  import { authStore } from '../../lib/store.js';

  // Svelte 4 Props
  export let onSuccess = () => {};

  // Standard local variables (Replaces $state)
  let mode = 'login';
  let firstName = '';
  let lastName = '';
  let email = '';
  let password = '';
  let role = 'Reader';
  let loading = false;
  let message = '';

  async function submit() {
    message = ''; 
    loading = true;
    try {
      if (mode === 'register') {
        // Calling Flask register endpoint
        await auth.register({ 
          first_name: firstName, 
          last_name: lastName, 
          email, 
          password, 
          role 
        });
        message = 'Account created. Logging you in…';
      }
      
      // Calling Flask login endpoint
      const data = await auth.login({ email, password });
      
      // Update global store
      authStore.setSession(data.access_token, data.user);
      onSuccess(data.user);
    } catch (err) {
      message = err.data?.msg || err.message || 'Authentication failed';
    } finally { 
      loading = false; 
    }
  }

  function toggleMode() {
    mode = mode === 'login' ? 'register' : 'login';
    message = '';
  }
</script>

<div class="h-32"></div>

<section class="max-w-xl mx-auto px-6 pb-20">
  <div class="glass-panel p-10 md:p-16 rounded-[3rem] space-y-10 shadow-2xl">
    <header class="text-center space-y-4">
      <p class="text-[10px] font-black text-blue-400 tracking-[0.3em] uppercase">Secure Access</p>
      <h1 class="text-4xl md:text-5xl font-black text-white">
        {mode === 'login' ? 'Welcome back' : 'Create account'}
      </h1>
      <p class="text-white/40 text-sm max-w-xs mx-auto">
        Access the student blogging community.
      </p>
    </header>

    <form on:submit|preventDefault={submit} class="space-y-4">
      {#if mode === 'register'}
        <div class="grid grid-cols-2 gap-4">
          <input bind:value={firstName} placeholder="First name" class="form-input" required />
          <input bind:value={lastName} placeholder="Last name" class="form-input" required />
        </div>
        
        <div class="space-y-2">
          <label class="text-[10px] font-bold text-white/40 uppercase tracking-widest ml-2">Account Role</label>
          <select bind:value={role} class="form-input">
            <option>Reader</option>
            <option>Writer</option>
            <option>Admin</option>
          </select>
        </div>
      {/if}

      <input type="email" bind:value={email} placeholder="Email address" required class="form-input" />
      <input type="password" bind:value={password} placeholder="Password" required minlength="3" class="form-input" />

      {#if message}
        <p class="bg-red-500/10 border border-red-500/20 text-red-400 p-4 rounded-2xl text-xs font-bold text-center animate-pulse">
          {message}
        </p>
      {/if}

      <button class="primary-btn w-full py-4 mt-4" disabled={loading}>
        {loading ? 'Authenticating...' : (mode === 'login' ? 'Login' : 'Register')}
      </button>
    </form>

    <div class="pt-6 border-t border-white/5 text-center">
      <button class="text-white/40 hover:text-blue-400 text-sm font-medium transition-colors" on:click={toggleMode}>
        {mode === 'login' ? "Don't have an account? Register" : "Already have an account? Login"}
      </button>
    </div>
  </div>
</section>

<style>
  @reference "../../app.css";
  .glass-panel {
    background-color: rgba(15, 18, 25, 0.7);
    backdrop-filter: blur(16px);
    border: 1px solid rgba(255, 255, 255, 0.08);
  }

  .form-input {
    @apply w-full bg-white/5 border border-white/10 rounded-2xl px-5 py-4 text-white placeholder-white/20 focus:outline-none focus:border-blue-500 transition-all;
  }

  .primary-btn {
    @apply bg-blue-600 hover:bg-blue-500 text-white rounded-2xl font-black uppercase tracking-widest text-xs transition-all shadow-lg shadow-blue-500/20 active:scale-95 disabled:opacity-50;
  }
</style>