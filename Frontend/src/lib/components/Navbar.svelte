<script>
  import { authStore } from '../store.js';
  import { onMount } from 'svelte';

  // Props
  export let activeTab = 'Home';
  export let onLogout = () => {};
  export let onSearch = () => {};

  const menuItems = ['Home', 'Read', 'Top Blogs', 'Guidelines', 'About'];

  // State
  let query = '';
  let profileOpen = false;
  let accessOpen = false;
  let mobileOpen = false;
  let isLargeText = false;

  function setTheme(theme) {
    document.documentElement.dataset.theme = theme;
    localStorage.setItem('theme', theme);
  }

  function toggleLargeText() {
    isLargeText = document.documentElement.classList.toggle('large-text');
    localStorage.setItem('large-text-enabled', isLargeText);
  }

  function nav(tab) {
    activeTab = tab;
    profileOpen = false;
    accessOpen = false;
    mobileOpen = false;
  }

  function submitSearch() {
    onSearch(query.trim());
    nav('Home');
  }

  function logout() {
    authStore.clearSession();
    onLogout();
    nav('Home');
  }

  onMount(() => {
    // Restore Large Text preference
    isLargeText = localStorage.getItem('large-text-enabled') === 'true';
    if (isLargeText) document.documentElement.classList.add('large-text');
    
    // Restore Theme preference
    const savedTheme = localStorage.getItem('theme') || 'dark';
    setTheme(savedTheme);
  });
</script>

<div class="fixed top-0 left-0 right-0 z-[100] flex justify-center pointer-events-none pt-4">
  <nav class="nav-container p-3 rounded-2xl flex items-center justify-between text-white shadow-2xl border w-[calc(100%-2rem)] max-w-5xl pointer-events-auto transition-colors duration-500">
    
    <div class="flex items-center gap-2 md:gap-6">
      <!-- Mobile Hamburger -->
      <button 
        on:click={() => mobileOpen = !mobileOpen} 
        class="md:hidden p-2 hover:bg-white/5 rounded-lg transition-colors"
        aria-label="Toggle Mobile Menu"
      >
          <div class="w-5 h-0.5 bg-white mb-1"></div>
          <div class="w-5 h-0.5 bg-white mb-1"></div>
          <div class="w-5 h-0.5 bg-white"></div>
      </button>

      <button on:click={() => nav('Home')} class="logo-box px-4 py-2 rounded-xl font-bold transition-all cursor-pointer tracking-tighter">
        STUD<span class="text-blue-400">BLOGS</span>
      </button>
      
      <ul class="hidden md:flex items-center gap-1 text-sm font-medium">
        {#each menuItems as item}
          <li>
            <button 
              on:click={() => nav(item)} 
              class="px-4 py-2 rounded-lg transition-all {activeTab === item ? 'bg-white/10 text-white' : 'text-gray-400 hover:text-white hover:bg-white/5'}"
            >
              {item}
            </button>
          </li>
        {/each}
      </ul>
    </div>

    <div class="flex items-center gap-2 md:gap-3">
      <form class="relative flex items-center" on:submit|preventDefault={submitSearch}>
        <input 
          type="text" 
          bind:value={query}
          placeholder="Search" 
          id="nav-search"
          class="search-input rounded-full py-1.5 pl-9 pr-4 text-sm outline-none w-24 sm:w-40 lg:w-48 focus:w-44 sm:focus:w-56 lg:focus:w-64 transition-all duration-300 text-white placeholder:text-gray-500 border border-white/5 focus:border-blue-500/50"
        />
        <label for="nav-search" class="absolute left-3 flex items-center pointer-events-none opacity-40">
          <span class="text-sm">⌕</span>
        </label>
      </form>

      <!-- Accessibility Menu -->
      <div class="relative">
        <button 
          on:click={() => { accessOpen = !accessOpen; profileOpen = false; }} 
          class="p-2.5 hover:bg-white/10 rounded-xl transition-colors {accessOpen ? 'bg-white/10 ring-1 ring-white/20' : ''}"
          aria-label="Accessibility Settings"
        >
          <span class="opacity-80 text-lg">♿</span>
        </button>

        {#if accessOpen}
          <div class="absolute right-0 mt-3 w-60 dropdown-panel rounded-2xl border border-white/10 shadow-2xl z-[110] flex flex-col overflow-hidden">
            <div class="p-4 border-b border-white/5 bg-white/5">
              <p class="text-[10px] font-black text-white/30 uppercase tracking-widest">Accessibility</p>
            </div>
            <div class="p-2 flex flex-col gap-1">
              <button on:click={() => setTheme('dark')} class="dropdown-btn">Dark Default</button>
              <button on:click={() => setTheme('warm')} class="dropdown-btn">Warm Mode</button>
              <button on:click={() => setTheme('contrast')} class="dropdown-btn">High Contrast</button>
              <div class="border-t border-white/5 my-1"></div>
              <button on:click={toggleLargeText} class="dropdown-btn text-blue-400 flex justify-between items-center">
                Large Text 
                <span class="text-[10px]">{isLargeText ? 'ON' : 'OFF'}</span>
              </button>
            </div>
          </div>
          <button on:click={() => accessOpen = false} class="fixed inset-0 z-[105] cursor-default" aria-label="Close menu" tabindex="-1"></button>
        {/if}
      </div>

      <!-- User Profile Menu -->
      <div class="relative">
        <button 
          on:click={() => { profileOpen = !profileOpen; accessOpen = false; }} 
          class="p-2.5 rounded-xl hover:bg-blue-600/30 border border-blue-500/10 transition-all {profileOpen ? 'bg-blue-600/40 ring-2 ring-blue-500/50' : 'bg-blue-600/20'}"
          aria-label="User Account"
        >
          <span class="text-lg">👤</span>
        </button>

        {#if profileOpen}
          <div class="absolute right-0 mt-3 w-64 dropdown-panel rounded-2xl border border-white/10 shadow-2xl z-[110] flex flex-col overflow-hidden">
            <div class="p-4 border-b border-white/5 bg-white/5">
              <p class="text-sm font-bold text-white leading-tight">
                {$authStore.isLoggedIn ? ($authStore.user?.first_name || 'User') : 'Guest'}
              </p>
              <p class="text-[10px] text-blue-400 uppercase tracking-widest font-semibold">
                {$authStore.isLoggedIn ? $authStore.user?.role : 'Visitor'}
              </p>
            </div>
            
            <div class="p-2 flex flex-col gap-1">
              {#if $authStore.isLoggedIn}
                <!-- Dynamic check for Writer or Admin -->
                {#if ['Writer', 'Admin'].includes($authStore.user?.role)}
                  <button on:click={() => nav('Write a Post')} class="dropdown-btn">Create Post</button>
                {/if}

                <!-- Dedicated Admin Panel button -->
                {#if $authStore.user?.role === 'Admin'}
                  <button 
                    on:click={() => nav('Admin Panel')} 
                    class="dropdown-btn text-yellow-400 border border-yellow-400/10 bg-yellow-400/5 mt-1 hover:bg-yellow-400/10"
                  >
                    🛡️ Admin Panel
                  </button>
                {/if}

                <button on:click={() => nav('Liked Posts')} class="dropdown-btn">Liked Posts</button>
                <button on:click={() => nav('Saved Posts')} class="dropdown-btn">Saved Posts</button>
                
                <div class="border-t border-white/5 my-1"></div>
                
                <button on:click={() => nav('Account Settings')} class="dropdown-btn">Account Settings</button>
                <button on:click={logout} class="dropdown-btn text-red-500 font-bold mt-1">Sign Out</button>
              {:else}
                <button on:click={() => nav('Register/Log-in')} class="dropdown-btn font-bold text-blue-400">Login / Register</button>
              {/if}
            </div>
          </div>
          <button on:click={() => profileOpen = false} class="fixed inset-0 z-[105] cursor-default" aria-label="Close menu" tabindex="-1"></button>
        {/if}
      </div>
    </div>

    <!-- Mobile Dropdown Menu -->
    {#if mobileOpen}
      <div class="absolute top-full left-0 right-0 mt-2 dropdown-panel backdrop-blur-xl rounded-2xl border border-white/10 p-2 flex flex-col gap-1 md:hidden shadow-2xl">
          {#each menuItems as item}
              <button 
                on:click={() => nav(item)} 
                class="w-full text-left px-4 py-3 rounded-xl transition-colors {activeTab === item ? 'bg-blue-500/20 text-blue-400' : 'hover:bg-white/5'}"
              >
                {item}
              </button>
          {/each}
      </div>
    {/if}
  </nav>
</div>

<style>
  :root {
    --nav-bg: rgba(30, 41, 59, 0.5); 
    --nav-border: rgba(255, 255, 255, 0.1);
    --dropdown-bg: rgba(26, 31, 46, 0.8);
    --logo-bg: rgba(51, 65, 85, 0.5);
    --search-bg: rgba(15, 23, 42, 0.3);
  }

  :root[data-theme='warm'] {
    --nav-bg: rgba(69, 39, 39, 0.5);
    --nav-border: rgba(251, 191, 36, 0.2);
    --dropdown-bg: rgba(45, 27, 27, 0.8);
    --logo-bg: rgba(90, 46, 78, 0.5);
    --search-bg: rgba(45, 27, 27, 0.3);
  }

  :root[data-theme='contrast'] {
    --nav-bg: rgba(0, 0, 0, 0.7);
    --nav-border: #ffffff;
    --dropdown-bg: rgba(0, 0, 0, 0.95);
    --logo-bg: rgba(34, 34, 34, 0.8);
    --search-bg: rgba(0, 0, 0, 0.6);
  }

  :root[data-theme] {
    background-color: transparent !important;
  }

  .nav-container {
    background-color: var(--nav-bg);
    border-color: var(--nav-border);
    backdrop-filter: blur(12px) saturate(180%);
    -webkit-backdrop-filter: blur(12px) saturate(180%);
    transition: background-color 0.5s ease, border-color 0.5s ease;
  }

  .dropdown-panel {
    background-color: var(--dropdown-bg);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    box-shadow: 0 20px 40px rgba(0, 0, 0, 0.4);
  }

  .logo-box {
    background-color: var(--logo-bg);
    backdrop-filter: blur(4px);
    border: 1px solid rgba(255, 255, 255, 0.05);
  }

  .search-input {
    background-color: var(--search-bg);
    backdrop-filter: blur(4px);
  }

  .dropdown-btn {
    width: 100%;
    text-align: left;
    padding: 0.625rem 0.75rem;
    font-size: 0.875rem;
    color: #d1d5db;
    border-radius: 0.5rem;
    transition: all 0.2s;
  }

  .dropdown-btn:hover {
    background-color: rgba(255, 255, 255, 0.1);
    color: white;
  }
</style>