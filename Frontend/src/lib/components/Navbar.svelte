<script>
  import UserIcon from '../../assets/Navbar/user.svg';
  import AcceIcon from '../../assets/Navbar/accessibility.svg';
  import SearchIcon from '../../assets/Navbar/search.svg';
</script>
<nav class="bg-slate-800/80 backdrop-blur-md m-4 p-3 rounded-2xl flex items-center justify-between text-white shadow-xl border border-white/5">
  
  <div class="flex items-center gap-6">
    <div class="bg-slate-700 px-6 py-2 rounded-xl font-bold tracking-tight">
      Logo
    </div>
    
    <ul class="flex items-center gap-6 text-sm font-medium">
      <li class="bg-white/10 px-4 py-1.5 rounded-lg cursor-pointer">Home</li>
      <li class="text-gray-400 hover:text-white transition cursor-pointer">Read</li>
      <li class="text-gray-400 hover:text-white transition cursor-pointer">Top Blogs</li>
      <li class="text-gray-400 hover:text-white transition cursor-pointer">Guidelines</li>
      <li class="text-gray-400 hover:text-white transition cursor-pointer">About</li>
    </ul>
  </div>

  <div class="flex items-center gap-3">
    <div class="relative sm:block">
      <input 
        type="text" 
        placeholder="Search" 
        style="padding-left: 2rem !important;"
        class="bg-slate-700 rounded-full py-1.5 px-4 text-sm outline-none w-48 focus:ring-2 ring-blue-500/50 transition-all text-white placeholder:text-gray-400"
      />
      <span class="absolute left-3 top-2.5 opacity-60">
        <img src={SearchIcon} class="size-4" alt="" />
      </span>
    </div>

    <button class="p-2 hover:bg-white/10 rounded-full transition-colors cursor-pointer">
      <img src={AcceIcon} class="size-5 brightness-200" alt="Accessibility" />
    </button>

    <button class="bg-purple-600/30 p-2 rounded-full hover:bg-purple-600/50 transition-colors cursor-pointer border border-purple-500/20">
      <img src={UserIcon} class="size-5 brightness-200" alt="User Profile" />
    </button>
  </div>
</nav>