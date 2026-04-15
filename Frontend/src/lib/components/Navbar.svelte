<script>
  import UserIcon from '../../assets/Navbar/user.svg';
  import AcceIcon from '../../assets/Navbar/accessibility.svg';
  import SearchIcon from '../../assets/Navbar/search.svg';

  // State for the active menu item
  let activeTab = "Home";
  const menuItems = ["Home", "Read", "Top Blogs", "Guidelines", "About"];

  // State for search
  let searchQuery = "";

  function handleSearch(e) {
    console.log("Searching for:", searchQuery);
    // You can add logic here to filter your posts later!
  }
</script>

<nav class="bg-slate-800/80 backdrop-blur-md mr-4 ml-4 p-3 rounded-br-xl rounded-bl-xl flex items-center justify-between text-white shadow-xl border border-white/5">
  
  <div class="flex items-center gap-6">
    <button 
      onclick={() => activeTab = "Home"}
      class="bg-slate-700 px-6 py-2 rounded-xl font-bold tracking-tight hover:bg-slate-600 transition-colors cursor-pointer"
    >
      Logo
    </button>
    
    <ul class="flex items-center gap-6 text-sm font-medium">
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
      <span class="absolute left-3 top-2.5 opacity-60 pointer-events-none">
        <img src={SearchIcon} class="size-4" alt="" />
      </span>
    </div>

    <button 
      onclick={() => alert('Accessibility menu coming soon!')}
      class="p-2 hover:bg-white/10 rounded-full transition-colors cursor-pointer group"
    >
      <img src={AcceIcon} class="size-5 brightness-200 opacity-70 group-hover:opacity-100" alt="Accessibility" />
    </button>

    <button 
      onclick={() => console.log('Open Profile')}
      class="bg-purple-600/30 p-2 rounded-full hover:bg-purple-600/50 transition-all cursor-pointer border border-purple-500/20 active:scale-90"
    >
      <img src={UserIcon} class="size-5 brightness-200" alt="User Profile" />
    </button>
  </div>
</nav>