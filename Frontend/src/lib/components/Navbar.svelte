<script>
  import UserIcon from '../../assets/Navbar/user.svg';
  import AcceIcon from '../../assets/Navbar/accessibility.svg';
  import SearchIcon from '../../assets/Navbar/search.svg';

  let { activeTab = $bindable("Home") } = $props();
  const menuItems = ["Home", "Read", "Top Blogs", "Guidelines", "About"];

  let searchQuery = $state("");
  let isProfileOpen = $state(false); 
  let isAcceOpen = $state(false);
  let isMobileMenuOpen = $state(false);

  let nickname = "Nickname";
  let role = "Admin";

  // Accessibility States
  let highContrast = $state(false);
  let largeText = $state(false);
  let dyslexiaFont = $state(false);

  function toggleProfile() {
    isProfileOpen = !isProfileOpen;
    if (isProfileOpen) { isAcceOpen = false; isMobileMenuOpen = false; }
  }

  function toggleAcce() {
    isAcceOpen = !isAcceOpen;
    if (isAcceOpen) { isProfileOpen = false; isMobileMenuOpen = false; }
  }

  function navigateTo(tabName) {
    activeTab = tabName;
    isProfileOpen = false;
    isAcceOpen = false;
    isMobileMenuOpen = false;
  }
</script>

<nav class="bg-slate-800/80 backdrop-blur-md mx-2 md:mx-4 p-3 rounded-b-xl flex items-center justify-between text-white shadow-xl border border-white/5 relative z-[100]">
  
  <div class="flex items-center gap-2 md:gap-6">
    <button onclick={() => isMobileMenuOpen = !isMobileMenuOpen} class="md:hidden p-2 hover:bg-white/5 rounded-lg">
        <div class="w-5 h-0.5 bg-white mb-1"></div>
        <div class="w-5 h-0.5 bg-white mb-1"></div>
        <div class="w-5 h-0.5 bg-white"></div>
    </button>

    <button onclick={() => navigateTo("Home")} class="bg-slate-700 px-4 py-2 rounded-xl font-bold hover:bg-slate-600 transition-colors cursor-pointer">
      Logo
    </button>
    
    <ul class="hidden md:flex items-center gap-2 text-sm font-medium">
      {#each menuItems as item}
        <li>
          <button onclick={() => navigateTo(item)} class="px-4 py-1.5 rounded-lg {activeTab === item ? 'bg-white/10 text-white' : 'text-gray-400 hover:text-white'}">
            {item}
          </button>
        </li>
      {/each}
    </ul>
  </div>

  <div class="flex items-center gap-2 md:gap-3">
    <div class="relative flex items-center">
    <input 
      type="text" 
      bind:value={searchQuery}
      placeholder="Search" 
      class="bg-slate-700 rounded-full py-1.5 pl-9 pr-4 text-sm outline-none 
             w-24 sm:w-40 lg:w-64 
             focus:w-44 sm:focus:w-64 lg:focus:w-80 
             transition-all duration-300 text-white placeholder:text-gray-400 
             border border-white/5 focus:border-blue-500/50"
    />
    <div class="absolute left-3 flex items-center pointer-events-none">
      <img src={SearchIcon} class="size-4 opacity-50 brightness-200" alt="" />
    </div>
  </div>

    <div class="relative">
      <button onclick={toggleAcce} class="p-2 hover:bg-white/10 rounded-full group {isAcceOpen ? 'bg-white/10' : ''}">
        <img src={AcceIcon} class="size-5 brightness-200 opacity-70" alt="" />
      </button>

      {#if isAcceOpen}
        <div class="absolute right-0 mt-3 w-72 bg-[#1A1F2E] rounded-2xl border border-white/10 shadow-2xl z-[110] overflow-visible">
          <div class="p-4 border-b border-white/5 bg-white/5 rounded-t-2xl">
            <p class="text-sm font-bold text-white">Accessibility</p>
          </div>
          <div class="p-3 flex flex-col gap-2">
            <button onclick={() => highContrast = !highContrast} class="flex items-center justify-between w-full p-2 hover:bg-white/5 rounded-xl transition-colors">
              <span class="text-xs text-gray-300">High Contrast</span>
              <div class="w-8 h-4 rounded-full relative {highContrast ? 'bg-blue-500' : 'bg-slate-700'}">
                <div class="absolute top-0.5 left-0.5 size-3 bg-white rounded-full transition-transform {highContrast ? 'translate-x-4' : ''}"></div>
              </div>
            </button>
            <button onclick={() => dyslexiaFont = !dyslexiaFont} class="flex items-center justify-between w-full p-2 hover:bg-white/5 rounded-xl transition-colors">
              <span class="text-xs text-gray-300">Dyslexia Font</span>
              <div class="w-8 h-4 rounded-full relative {dyslexiaFont ? 'bg-blue-500' : 'bg-slate-700'}">
                <div class="absolute top-0.5 left-0.5 size-3 bg-white rounded-full transition-transform {dyslexiaFont ? 'translate-x-4' : ''}"></div>
              </div>
            </button>
          </div>
        </div>
        <button onclick={toggleAcce} class="fixed inset-0 z-[105] cursor-default bg-transparent w-full h-full" tabindex="-1"></button>
      {/if}
    </div>

    <div class="relative">
      <button onclick={toggleProfile} class="bg-purple-600/30 p-2 rounded-full hover:bg-purple-600/50 border border-purple-500/20 {isProfileOpen ? 'ring-2 ring-purple-500' : ''}">
        <img src={UserIcon} class="size-5 brightness-200" alt="" />
      </button>

      {#if isProfileOpen}
        <div class="absolute right-0 mt-3 w-64 bg-[#1A1F2E] rounded-2xl border border-white/10 shadow-2xl z-[110] flex flex-col overflow-hidden">
          <div class="p-4 border-b border-white/5 bg-white/5">
            <p class="text-sm font-bold text-white">{nickname}</p>
            <p class="text-[10px] text-purple-400 uppercase tracking-widest">{role}</p>
          </div>
          <div class="p-2 flex flex-col gap-1">
            <button onclick={() => navigateTo("Register/Log-in")} class="w-full text-left px-3 py-2 text-sm text-gray-400 hover:bg-white/5 rounded-lg transition-colors">Login</button>
            <div class="border-t border-white/5 my-1"></div>
            <button onclick={() => navigateTo("Write a Post")} class="w-full text-left px-3 py-2 text-sm text-gray-200 hover:bg-white/5 rounded-lg transition-colors">Write Post</button>
            <button onclick={() => navigateTo("Liked Posts")} class="w-full text-left px-3 py-2 text-sm text-gray-200 hover:bg-white/5 rounded-lg transition-colors">Liked Posts</button>
            <button onclick={() => navigateTo("Saved Posts")} class="w-full text-left px-3 py-2 text-sm text-gray-200 hover:bg-white/5 rounded-lg transition-colors">Saved Posts</button>
            <div class="border-t border-white/5 my-1"></div>
            <button onclick={() => navigateTo("Account Settings")} class="w-full text-left px-3 py-2 text-sm text-gray-400 hover:bg-white/5 rounded-lg transition-colors">Settings</button>
            {#if role === "Admin"}
              <button onclick={() => navigateTo("Management Panel")} class="w-full text-left px-3 py-2 text-sm text-red-400 hover:bg-red-500/10 rounded-lg transition-colors">Admin Panel</button>
            {/if}
          </div>
        </div>
        <button onclick={toggleProfile} class="fixed inset-0 z-[105] cursor-default bg-transparent w-full h-full" tabindex="-1"></button>
      {/if}
    </div>
  </div>

  {#if isMobileMenuOpen}
    <div class="absolute top-full left-0 right-0 mt-2 bg-[#1A1F2E] rounded-2xl border border-white/10 mx-2 p-2 flex flex-col gap-1 md:hidden shadow-2xl z-[110]">
        {#each menuItems as item}
            <button onclick={() => navigateTo(item)} class="w-full text-left px-4 py-3 rounded-xl hover:bg-white/5">{item}</button>
        {/each}
    </div>
  {/if}
</nav>