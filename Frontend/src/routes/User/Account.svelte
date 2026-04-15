<script>
  // Svelte 5 state for form management
  let name = $state("John Doe");
  let nickname = $state("Nickname");
  let email = $state("john.doe@university.edu");
  let bio = $state("Computer Science student at TU Delft. Passionate about AI and web design.");
  
  // Handlers
  function handleSave() {
    console.log("Saving changes for:", nickname);
  }

  function handleAvatarChange() {
    console.log("Opening file picker...");
  }
</script>

<div class="h-32"></div>

<section class="max-w-5xl mx-auto px-6 mb-20 animate-in fade-in slide-in-from-bottom-6 duration-700">
  
  <div class="mb-10">
    <p class="text-[10px] font-black text-purple-400 tracking-widest uppercase mb-2">Personalization</p>
    <h1 class="text-4xl font-bold text-white">Account Settings</h1>
  </div>

  <div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
    
    <div class="bg-[#1A1F2E] p-8 rounded-[2.5rem] border border-white/5 flex flex-col items-center text-center shadow-2xl">
      <div class="relative group cursor-pointer" onclick={handleAvatarChange}>
        <div class="size-32 bg-purple-600 rounded-full flex items-center justify-center text-4xl text-white font-bold mb-6 border-4 border-white/5 group-hover:brightness-75 transition-all">
          JD
        </div>
        <div class="absolute inset-0 flex items-center justify-center opacity-0 group-hover:opacity-100 transition-opacity">
          <span class="text-[10px] font-black text-white uppercase bg-black/50 px-3 py-1 rounded-full">Change</span>
        </div>
      </div>
      
      <h2 class="text-xl font-bold text-white mb-1">{nickname}</h2>
      <p class="text-xs text-purple-400 font-black uppercase tracking-widest mb-6">Writer</p>
      
      <div class="w-full pt-6 border-t border-white/5">
        <p class="text-[10px] text-gray-500 uppercase font-bold mb-2">Bio</p>
        <p class="text-sm text-gray-400 leading-relaxed italic">"{bio}"</p>
      </div>
    </div>

    <div class="lg:col-span-2 space-y-6">
      
      <div class="bg-[#1A1F2E] p-8 rounded-[2.5rem] border border-white/5 shadow-2xl">
        <h3 class="text-sm font-bold text-white mb-6 uppercase tracking-wider flex items-center gap-2">
           <span class="size-2 bg-blue-500 rounded-full"></span> Public Profile
        </h3>
        
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
          <div class="flex flex-col gap-2">
            <label class="text-[10px] text-gray-500 uppercase font-black ml-1">Full Name</label>
            <input bind:value={name} class="bg-white/5 border border-white/10 rounded-xl px-4 py-3 text-sm text-white outline-none focus:ring-2 ring-blue-500/50 transition-all" />
          </div>
          <div class="flex flex-col gap-2">
            <label class="text-[10px] text-gray-500 uppercase font-black ml-1">Nickname</label>
            <input bind:value={nickname} class="bg-white/5 border border-white/10 rounded-xl px-4 py-3 text-sm text-white outline-none focus:ring-2 ring-blue-500/50 transition-all" />
          </div>
        </div>
      </div>

      <div class="bg-[#1A1F2E] p-8 rounded-[2.5rem] border border-white/5 shadow-2xl">
        <h3 class="text-sm font-bold text-white mb-6 uppercase tracking-wider flex items-center gap-2">
           <span class="size-2 bg-green-500 rounded-full"></span> Contact Details
        </h3>
        
        <div class="flex flex-col gap-2">
          <label class="text-[10px] text-gray-500 uppercase font-black ml-1">Email Address</label>
          <div class="flex gap-4">
            <input bind:value={email} class="flex-grow bg-white/5 border border-white/10 rounded-xl px-4 py-3 text-sm text-white outline-none focus:ring-2 ring-green-500/50 transition-all" />
            <button class="bg-white/5 border border-white/10 px-4 rounded-xl text-[10px] font-black text-gray-400 hover:text-white transition-colors">Verify</button>
          </div>
        </div>
      </div>

      <div class="flex justify-end gap-4">
        <button class="px-8 py-3 rounded-xl text-sm font-bold text-gray-500 hover:text-white transition-colors">Discard</button>
        <button onclick={handleSave} class="px-8 py-3 bg-purple-600 hover:bg-purple-500 text-white rounded-xl text-sm font-bold shadow-lg shadow-purple-900/20 transition-all active:scale-95">
          Save Changes
        </button>
      </div>

    </div>
  </div>
</section>