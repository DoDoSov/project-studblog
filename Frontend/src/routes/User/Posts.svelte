<script>
  import { onMount } from 'svelte';
  import { posts as postsApi } from '../../lib/api.js';
  import { authStore } from '../../lib/store.js';
  import { CATEGORIES, formatDate } from '../../lib/utils.js';

  export let onPostClick = () => {};

  let myPosts = [];
  let loading = true;
  let fetchError = '';
  let editingId = null;
  let saving = false;
  let saveError = '';

  let title = '', category = 'Technology', description = '', imageUrl = '', content = '';
  let editorElement, quill;

  onMount(async () => {
    const Quill = (await import('quill')).default;
    import('quill/dist/quill.snow.css');
    quill = new Quill(editorElement, {
      theme: 'snow',
      modules: { toolbar: [[{ 'header': [1, 2, false] }], ['bold', 'italic'], ['link', 'image'], ['clean']] }
    });
    quill.on('text-change', () => { content = quill.root.innerHTML; });
  });

  $: if ($authStore.isLoggedIn) load();

  async function load() {
    loading = true;
    try { myPosts = await postsApi.mine(); } 
    catch (e) { fetchError = e.message; } 
    finally { loading = false; }
  }

  async function save() {
    saving = true;
    saveError = '';
    const payload = { title, category, description, banner_url: imageUrl, content };

    try {
      if (editingId) { await postsApi.update(editingId, payload); } 
      else { await postsApi.create(payload); }
      reset();
      await load();
    } catch (e) { saveError = e.data?.msg || e.message; } 
    finally { saving = false; }
  }

  function reset() {
    editingId = null; title = ''; description = ''; imageUrl = ''; content = '';
    if (quill) quill.root.innerHTML = '';
    category = 'Technology';
  }

  async function edit(post) {
    const full = await postsApi.get(post.id);
    editingId = full.id;
    title = full.title; category = full.category; description = full.description;
    imageUrl = full.banner_url; content = full.content;
    if (quill) quill.root.innerHTML = content;
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }

  async function remove(id) {
    if (confirm('Delete this post?')) {
      await postsApi.remove(id);
      await load();
    }
  }
</script>

<div class="h-32"></div>
<section class="max-w-7xl mx-auto px-6 pb-20">
  {#if !$authStore.isLoggedIn}
    <div class="glass-panel p-20 text-center rounded-[3rem]">Please log in.</div>
  {:else}
    <div class="grid grid-cols-1 lg:grid-cols-3 gap-12">
      <form class="lg:col-span-2 glass-panel p-10 rounded-[2.5rem] space-y-6" on:submit|preventDefault={save}>
        <h1 class="text-4xl font-black text-white">{editingId ? 'Update Post' : 'New Article'}</h1>
        <div class="grid grid-cols-2 gap-6">
          <input bind:value={title} placeholder="Title" required class="form-input" />
          <select bind:value={category} class="form-input">
            {#each CATEGORIES.filter(c => c !== 'All') as c}<option>{c}</option>{/each}
          </select>
        </div>
        <input bind:value={imageUrl} placeholder="Image URL" class="form-input" />
        <textarea bind:value={description} placeholder="Short summary..." class="form-input"></textarea>
        <div class="editor-wrapper"><div bind:this={editorElement}></div></div>
        <button class="bg-blue-600 w-full py-4 rounded-2xl font-bold text-white transition-all disabled:opacity-50" disabled={saving}>
          {saving ? 'Saving...' : 'Submit for Review'}
        </button>
      </form>

      <div class="glass-panel p-10 rounded-[2.5rem] space-y-6">
        <h2 class="text-xl font-bold text-white uppercase tracking-widest border-b border-white/10 pb-4">My Archive</h2>
        <div class="space-y-4 max-h-[800px] overflow-y-auto custom-scrollbar">
          {#each myPosts as post}
            <div class="bg-white/5 p-5 rounded-2xl border border-white/5">
              <div class="flex justify-between items-start mb-2">
                <span class="text-[10px] font-bold uppercase px-2 py-1 rounded 
                  {post.status === 'Approved' ? 'bg-green-500/20 text-green-400' : 'bg-yellow-500/20 text-yellow-400'}">
                  {post.status || 'Pending'}
                </span>
                <small class="text-white/20">{formatDate(post.created_at)}</small>
              </div>
              <h3 class="text-white font-bold line-clamp-1 mb-4">{post.title}</h3>
              <div class="flex gap-2">
                <button class="flex-1 bg-white/5 py-2 rounded-lg text-xs font-bold" on:click={() => edit(post)}>Edit</button>
                <button class="flex-1 bg-red-500/10 text-red-400 py-2 rounded-lg text-xs font-bold" on:click={() => remove(post.id)}>Delete</button>
              </div>
            </div>
          {/each}
        </div>
      </div>
    </div>
  {/if}
</section>

<style>
  @reference "../../app.css";
  .glass-panel { background: rgba(15, 18, 25, 0.8); backdrop-filter: blur(20px); border: 1px solid rgba(255,255,255,0.1); }
  .form-input { @apply w-full bg-white/5 border border-white/10 rounded-2xl px-4 py-3 text-white focus:border-blue-500 outline-none; }
  .editor-wrapper { @apply bg-white/5 border border-white/10 rounded-2xl min-h-[300px]; }
  :global(.ql-editor) { color: white !important; }
  :global(.ql-toolbar) { background: #1a1f2e !important; border: none !important; }
</style>