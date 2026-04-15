<script>
  import { goto } from '$app/navigation';
</script>

<nav class="flex justify-between p-4 bg-[#1a1d35] border-b border-gray-700">
  <div class="font-bold text-white cursor-pointer" on:click={()=>goto('/') }>
    <span class="text-indigo-400">Stud</span>Blogs
  </div>

  <div class="hidden md:flex gap-3">
    <button on:click={()=>goto('/')} class="text-white">Home</button>
    <button on:click={()=>goto('/about')} class="text-gray-400">About</button>
  </div>
</nav>