<script>
  import UserIcon from '../../assets/Navbar/user.svg';
  import AcceIcon from '../../assets/Navbar/accessibility.svg';
  import SearchIcon from '../../assets/Navbar/search.svg';

  // --- Navigation State ---
  let { activeTab = $bindable("Home") } = $props();
  const menuItems = ["Home", "Read", "Top Blogs", "Guidelines", "About"];

  // --- Search State ---
  let searchQuery = "";

  function handleSearch() {
    console.log("Searching for:", searchQuery);
  }

  let isProfileOpen = $state(false); 
  let nickname = "Nickname";
  let role = "Admin";

  function toggleProfile() {
    isProfileOpen = !isProfileOpen;
    if (isProfileOpen) isAcceOpen = false; // Close accessibility if profile opens
  }

  // --- Accessibility Dropdown State ---
  let isAcceOpen = $state(false); 
  
  // These also need $state if you want the toggles to visually move
  let highContrast = $state(false);
  let largeText = $state(false);
  let dyslexiaFont = $state(false);

  function toggleAcce() {
    isAcceOpen = !isAcceOpen;
    if (isAcceOpen) isProfileOpen = false; // Close profile if accessibility opens
  }
</script>

<nav class="bg-slate-800/80 backdrop-blur-md mx-4 p-3 rounded-b-xl flex items-center justify-between text-white shadow-xl border border-white/5 relative z-50">
  
  <div class="flex items-center gap-6">
    <button 
      onclick={() => activeTab = "Home"}
      class="bg-slate-700 px-6 py-2 rounded-xl font-bold tracking-tight hover:bg-slate-600 transition-colors cursor-pointer"
    >
      Logo
    </button>
    
    <ul class="flex items-center gap-2 text-sm font-medium">
      {#each menuItems as item}
        <li>
          <button 
            onclick={() => activeTab = item}
            class="transition-all duration-200 cursor-pointer rounded-lg px-4 py-1.5
            {activeTab === item 
              ? 'bg-white/10 text-white shadow-inner' 
              : 'text-gray-400 hover:text-white hover:bg-white/5'}"
          >
            {item}
          </button>
        </li>
      {/each}
    </ul>
  </div>

  <div class="flex items-center gap-3">
    
    <div class="relative sm:block">
      <input 
        type="text" 
        bind:value={searchQuery}
        oninput={handleSearch}
        placeholder="Search" 
        class="bg-slate-700 rounded-full py-1.5 pl-10 pr-4 text-sm outline-none w-48 focus:ring-2 ring-blue-500/50 transition-all text-white placeholder:text-gray-400"
      />
      <img src={SearchIcon} class="absolute left-3 top-2.5 size-4 opacity-60 pointer-events-none" alt="" />
    </div>

    <div class="relative">
  <button 
    onclick={toggleAcce}
    class="p-2 hover:bg-white/10 rounded-full transition-colors cursor-pointer group {isAcceOpen ? 'bg-white/10' : ''}"
  >
    <img src={AcceIcon} class="size-5 brightness-200 opacity-70 group-hover:opacity-100" alt="Accessibility" />
  </button>

  {#if isAcceOpen}
    <div class="absolute right-0 mt-3 w-72 bg-[#1A1F2E] rounded-2xl border border-white/10 shadow-2xl z-50 overflow-hidden">
      
      <div class="p-4 border-b border-white/5 bg-white/5">
        <p class="text-sm font-bold text-white">Accessibility Settings</p>
        <p class="text-[10px] text-gray-400 mt-1 uppercase tracking-wider">Optimize your experience</p>
      </div>

      <div class="p-3 flex flex-col gap-2">
        
        <div class="flex items-center justify-between px-3 py-2 rounded-xl hover:bg-white/5 transition-colors">
          <div class="flex flex-col">
            <span class="text-sm text-gray-200 font-medium">High Contrast</span>
            <span class="text-[10px] text-gray-500">Sharper colors & borders</span>
          </div>
          <button 
            onclick={() => highContrast = !highContrast}
            class="w-10 h-5 rounded-full transition-colors relative {highContrast ? 'bg-blue-500' : 'bg-slate-700'}"
          >
            <div class="absolute top-1 left-1 size-3 bg-white rounded-full transition-transform {highContrast ? 'translate-x-5' : ''}"></div>
          </button>
        </div>

        <div class="flex items-center justify-between px-3 py-2 rounded-xl hover:bg-white/5 transition-colors">
          <div class="flex flex-col">
            <span class="text-sm text-gray-200 font-medium">Large Text</span>
            <span class="text-[10px] text-gray-500">Increase font sizes</span>
          </div>
          <button 
            onclick={() => largeText = !largeText}
            class="w-10 h-5 rounded-full transition-colors relative {largeText ? 'bg-blue-500' : 'bg-slate-700'}"
          >
            <div class="absolute top-1 left-1 size-3 bg-white rounded-full transition-transform {largeText ? 'translate-x-5' : ''}"></div>
          </button>
        </div>

        <div class="flex items-center justify-between px-3 py-2 rounded-xl hover:bg-white/5 transition-colors">
          <div class="flex flex-col">
            <span class="text-sm text-gray-200 font-medium">Dyslexia Font</span>
            <span class="text-[10px] text-gray-500">Easier to read typeface</span>
          </div>
          <button 
            onclick={() => dyslexiaFont = !dyslexiaFont}
            class="w-10 h-5 rounded-full transition-colors relative {dyslexiaFont ? 'bg-blue-500' : 'bg-slate-700'}"
          >
            <div class="absolute top-1 left-1 size-3 bg-white rounded-full transition-transform {dyslexiaFont ? 'translate-x-5' : ''}"></div>
          </button>
        </div>

      </div>

      <div class="p-3 bg-white/5 border-t border-white/5">
        <button class="w-full py-2 text-xs font-bold text-gray-400 hover:text-white transition-colors">
          Reset to Default
        </button>
      </div>
    </div>

        <button 
          onclick={toggleAcce}
          class="fixed inset-0 h-full w-full cursor-default z-40 bg-transparent"
          tabindex="-1">
        </button>
      {/if}
    </div>

    <div class="relative">
      <button 
        onclick={toggleProfile}
        class="bg-purple-600/30 p-2 rounded-full hover:bg-purple-600/50 transition-all cursor-pointer border border-purple-500/20 active:scale-95"
      >
        <img src={UserIcon} class="size-5 brightness-200" alt="User Profile" />
      </button>

      {#if isProfileOpen}
        <div class="absolute right-0 mt-3 w-64 bg-[#1A1F2E] rounded-2xl border border-white/10 shadow-2xl z-50 overflow-hidden">
          
          <div class="p-4 border-b border-white/5 bg-white/5">
            <p class="text-sm font-bold text-white">{nickname}</p>
            <p class="text-[10px] font-medium text-purple-400 tracking-widest uppercase mt-0.5">{role}</p>
          </div>

          <div class="p-2 flex flex-col gap-1">

            <button class="flex items-center gap-3 px-3 py-2 text-sm text-gray-400 hover:text-white hover:bg-white/5 rounded-xl transition-colors text-left">
               Register/Log-in
            </button>

            <div class="my-1 border-t border-white/5"></div>

            <button class="flex items-center gap-3 px-3 py-2 text-sm text-gray-300 hover:text-white hover:bg-white/5 rounded-xl transition-colors text-left">
               Write a Post
            </button>
            
            <button class="flex items-center gap-3 px-3 py-2 text-sm text-gray-300 hover:text-white hover:bg-white/5 rounded-xl transition-colors text-left">
               Liked Posts
            </button>

            <button class="flex items-center gap-3 px-3 py-2 text-sm text-gray-300 hover:text-white hover:bg-white/5 rounded-xl transition-colors text-left">
               Saved Posts
            </button>

            <div class="my-1 border-t border-white/5"></div>

            <button class="flex items-center gap-3 px-3 py-2 text-sm text-gray-400 hover:text-white hover:bg-white/5 rounded-xl transition-colors text-left">
               Account Settings
            </button>
            <div class="my-1 border-t border-white/5"></div>
            <button class="flex items-center gap-3 px-3 py-2 text-sm text-gray-400 hover:text-white hover:bg-white/5 rounded-xl transition-colors text-left">
               Management Panel
            </button>
          </div>
        </div>

        <button 
          onclick={toggleProfile}
          class="fixed inset-0 h-full w-full cursor-default z-40 bg-transparent outline-none"
          tabindex="-1">
        </button>
      {/if}
    </div>
  </div>
</nav>