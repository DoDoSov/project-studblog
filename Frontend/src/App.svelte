<script>
  import { onMount } from 'svelte';

  let view = 'home';
  let mobileMenu = false;
  let mobileSearch = false;
  let toast = '';
  let showToastFlag = false;

  function navigate(v) {
    view = v;
    window.scrollTo(0,0);
  }

  function toggleMobileMenu() {
    mobileMenu = !mobileMenu;
  }

  function toggleMobileSearch() {
    mobileSearch = !mobileSearch;
  }

  function showToastMsg(msg) {
    toast = msg;
    showToastFlag = true;
    setTimeout(()=> showToastFlag = false, 2500);
  }

  function likePost(post) {
    post.liked = !post.liked;
    post.likes += post.liked ? 1 : -1;
  }

  let posts = [
    { id:'js', title:'Getting Started with JavaScript in 2026', likes:142, liked:false },
    { id:'react', title:'Why React Still Dominates Frontend Development', likes:89, liked:false },
    { id:'api', title:'Understanding REST APIs', likes:203, liked:false }
  ];
</script>

<nav class="sticky top-0 z-50 flex items-center justify-between px-4 h-14 border-b border-navy-border bg-navy">
  <div class="font-bold text-white cursor-pointer" on:click={()=>navigate('home')}>
    <span class="text-indigo-400">Stud</span>Blogs
  </div>

  <div class="hidden md:flex gap-2">
    <button class="px-3 py-1 rounded-full bg-indigo-600 text-white" on:click={()=>navigate('home')}>Home</button>
    <button class="px-3 py-1 text-gray-300" on:click={()=>navigate('about')}>About</button>
  </div>

  <div class="md:hidden flex gap-2">
    <button on:click={toggleMobileSearch}>🔍</button>
    <button on:click={toggleMobileMenu}>☰</button>
  </div>
</nav>

{#if mobileSearch}
  <div class="p-2 bg-gray-800">
    <input class="w-full p-2 rounded bg-gray-700 text-white" placeholder="Search..." />
  </div>
{/if}

{#if mobileMenu}
  <div class="p-3 bg-gray-800 flex flex-col gap-2">
    <button on:click={()=>navigate('home')}>Home</button>
    <button on:click={()=>navigate('about')}>About</button>
  </div>
{/if}

{#if view === 'home'}
  <div class="p-4 grid md:grid-cols-3 gap-4">
    {#each posts as post}
      <div class="bg-gray-800 p-4 rounded-xl border border-gray-700">
        <h3 class="font-bold text-white mb-2">{post.title}</h3>
        <div class="flex justify-between items-center">
          <button on:click={()=>likePost(post)} class="text-sm">
            {post.liked ? '❤️' : '🤍'} {post.likes}
          </button>
          <button class="bg-indigo-600 px-3 py-1 rounded text-sm" on:click={()=>navigate('post')}>
            Read
          </button>
        </div>
      </div>
    {/each}
  </div>
{/if}

{#if view === 'post'}
  <div class="p-4 max-w-2xl mx-auto">
    <button class="mb-4 text-sm" on:click={()=>navigate('home')}>← Back</button>
    <h1 class="text-xl font-bold mb-2">Getting Started with JavaScript</h1>
    <p class="text-gray-400">This is a sample post content in Svelte version.</p>
  </div>
{/if}

{#if view === 'about'}
  <div class="p-4 max-w-2xl mx-auto">
    <h1 class="text-xl font-bold mb-2">About StudBlogs</h1>
    <p class="text-gray-400">Student blogging platform built with Svelte.</p>
  </div>
{/if}

{#if showToastFlag}
  <div class="fixed bottom-4 right-4 bg-indigo-600 text-white px-4 py-2 rounded">
    {toast}
  </div>
{/if}

<style>
  :global(body) {
    background: #1a1d35;
    color: white;
  }
</style>