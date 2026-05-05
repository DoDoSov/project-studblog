<script>
  import { me as meApi } from '../../lib/api.js';
  import { authStore } from '../../lib/store.js';

  // Standard variable declarations (Replaces $state)
  let firstName = '';
  let lastName  = '';
  let email     = '';
  let loading   = true;
  let saving     = false;
  let msg       = '';

  // Reactive logic for initial data fetch (Replaces $effect)
  $: if ($authStore.isLoggedIn) {
    loadUserData();
  } else {
    loading = false;
  }

  async function loadUserData() {
    try {
      const u = await meApi.get();
      firstName = u.first_name ?? '';
      lastName  = u.last_name  ?? '';
      email     = u.email      ?? '';
    } catch (err) {
      console.error("Failed to load user profile", err);
    } finally {
      loading = false;
    }
  }

  async function handleSave() {
    saving = true;
    msg    = '';
    try {
      await meApi.update({ first_name: firstName, last_name: lastName });
      // Update global session in store
      authStore.setSession($authStore.token, { 
        ...$authStore.user, 
        first_name: firstName, 
        last_name: lastName 
      });
      msg = 'Changes saved!';
    } catch (err) {
      msg = err.data?.msg ?? 'Save failed';
    } finally {
      saving = false;
    }
  }

  // Reactive declaration for initials (Replaces $derived)
  $: initials = (firstName[0] ?? '') + (lastName[0] ?? '') || (email[0] ?? '?');
</script>

<div class="h-32"></div>

<section class="max-w-5xl mx-auto px-6 mb-20 animate-in fade-in slide-in-from-bottom-6 duration-700">
  {#if !$authStore.isLoggedIn}
    <div class="glass-panel py-20 text-center text-gray-400 rounded-[3rem]">
      Please log in to view account settings.
    </div>
  {:else if loading}
    <div class="py-20 flex justify-center">
      <div class="size-10 border-2 border-blue-500 border-t-transparent rounded-full animate-spin"></div>
    </div>
  {:else}
    <div class="mb-10">
      <p class="text-[10px] font-black text-blue-400 tracking-[0.3em] uppercase mb-4">Personalization</p>
      <h1 class="text-5xl font-black text-white leading-tight">Account Settings</h1>
    </div>

    <div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
      <!-- Profile Card -->
      <div class="glass-panel p-8 rounded-[2.5rem] flex flex-col items-center text-center">
        <div class="size-32 bg-blue-600 rounded-full flex items-center justify-center text-4xl text-white font-bold mb-6 border-4 border-white/5 uppercase">
          {initials}
        </div>
        <h2 class="text-xl font-bold text-white mb-1">{firstName} {lastName}</h2>
        <p class="text-xs text-blue-400 font-black uppercase tracking-widest mb-6">
          {$authStore.user?.role ?? 'Reader'}
        </p>
      </div>

      <!-- Settings Form -->
      <div class="lg:col-span-2 space-y-6">
        <div class="glass-panel p-8 rounded-[2.5rem]">
          <h3 class="text-sm font-bold text-white mb-6 uppercase tracking-wider flex items-center gap-2">
            <span class="size-2 bg-blue-500 rounded-full"></span> Public Profile
          </h3>
          <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div class="flex flex-col gap-2">
              <label class="text-[10px] text-white/40 uppercase font-black ml-1">First Name</label>
              <input bind:value={firstName} class="form-input" />
            </div>
            <div class="flex flex-col gap-2">
              <label class="text-[10px] text-white/40 uppercase font-black ml-1">Last Name</label>
              <input bind:value={lastName} class="form-input" />
            </div>
          </div>
        </div>

        <div class="glass-panel p-8 rounded-[2.5rem]">
          <h3 class="text-sm font-bold text-white mb-6 uppercase tracking-wider flex items-center gap-2">
            <span class="size-2 bg-green-500 rounded-full"></span> Contact Details
          </h3>
          <div class="flex flex-col gap-2">
            <label class="text-[10px] text-white/40 uppercase font-black ml-1">Email Address</label>
            <input value={email} readonly class="form-input-readonly" />
          </div>
        </div>

        {#if msg}
          <p class="text-sm {msg.includes('saved') ? 'text-green-400' : 'text-red-400'} text-right font-bold animate-pulse">
            {msg}
          </p>
        {/if}

        <div class="flex justify-end gap-4">
          <button on:click={handleSave} disabled={saving} class="primary-btn px-10">
            {saving ? 'Saving…' : 'Save Changes'}
          </button>
        </div>
      </div>
    </div>
  {/if}
</section>

<style>
  @reference "../../app.css"; 
  .glass-panel {
    background-color: rgba(15, 18, 25, 0.7);
    backdrop-filter: blur(16px);
    border: 1px solid rgba(255, 255, 255, 0.08);
  }

  .form-input {
    @apply bg-white/5 border border-white/10 rounded-xl px-4 py-3 text-sm text-white outline-none focus:ring-2 ring-blue-500/50 transition-all;
  }

  .form-input-readonly {
    @apply flex-grow bg-white/5 border border-white/10 rounded-xl px-4 py-3 text-sm text-white/30 outline-none cursor-not-allowed;
  }

  .primary-btn {
    @apply py-3 bg-blue-600 hover:bg-blue-500 disabled:opacity-50 text-white rounded-xl text-sm font-bold shadow-lg shadow-blue-500/10 transition-all active:scale-95;
  }
</style>