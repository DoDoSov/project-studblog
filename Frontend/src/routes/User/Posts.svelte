<script>
  import { onMount, tick } from 'svelte';
  import { posts as postsApi } from '../../lib/api.js';
  import { authStore } from '../../lib/store.js';
  import { CATEGORIES, formatDate } from '../../lib/utils.js';

  let myPosts = [];
  let loading = true;
  let fetchError = '';
  
  let writingTip = "Loading daily inspiration...";

  // Form State
  let editingId = null;
  let saving = false;
  let saveError = '';
  let title = '', category = 'Technology', description = '', imageUrl = '', content = '';
  let github_repo = ''; 

  let editorElement, quill;

  onMount(async () => {
    try {
      const tipRes = await fetch('https://api.adviceslip.com/advice');
      const tipData = await tipRes.json();
      writingTip = tipData.slip.advice;
    } catch (e) {
      writingTip = "Write every day, even if it's just one sentence.";
    }

    const Quill = (await import('quill')).default;
    import('quill/dist/quill.snow.css');
    
    quill = new Quill(editorElement, {
      theme: 'snow',
      modules: { 
        toolbar: [
          [{ 'header': [1, 2, false] }],
          ['bold', 'italic', 'underline'],
          ['link', 'image', 'blockquote'],
          [{ 'list': 'ordered'}, { 'list': 'bullet' }],
          ['clean']
        ] 
      }
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

    // --- UPDATED GITHUB LOGIC ---
    // We now send github_repo as a clean, separate field to the backend.
    // The backend regex logic will look for it in the content, so we 
    // ensure the tag is present for the backend to sync properly.
    let cleanContent = content.replace(/\[github:\s*.*?\]/g, '').trim();
    let finalContent = cleanContent;
    if (github_repo.trim()) {
      finalContent += `<p>[github: ${github_repo.trim()}]</p>`;
    }

    const payload = { 
      title, 
      category, 
      description, 
      banner_url: imageUrl, 
      content: finalContent,
      github_repo: github_repo.trim() // Explicitly sending the column data
    };

    try {
      if (editingId) { await postsApi.update(editingId, payload); } 
      else { await postsApi.create(payload); }
      reset();
      await load();
    } catch (e) { 
      saveError = e.data?.msg || e.message; 
    } finally { 
      saving = false; 
    }
  }

  function reset() {
    editingId = null; title = ''; description = ''; imageUrl = ''; content = '';
    github_repo = ''; 
    if (quill) quill.root.innerHTML = '';
    category = 'Technology';
  }

  async function edit(post) {
    try {
      const full = await postsApi.get(post.id);
      editingId = full.id;
      title = full.title; 
      category = full.category; 
      description = full.description;
      imageUrl = full.banner_url; 
      
      // Load the repository name directly from the new database column
      github_repo = full.github_repo || '';
      
      // Clean the content for the editor (strip the tag so the user doesn't see it in Quill)
      let rawContent = full.content || '';
      content = rawContent.replace(/\[github:\s*.*?\]/g, '').trim();
      
      if (quill) quill.root.innerHTML = content;
      window.scrollTo({ top: 0, behavior: 'smooth' });
    } catch (e) {
      alert("Failed to load post for editing.");
    }
  }

  async function remove(id) {
    if (!confirm('Are you sure you want to permanently delete this post?')) return;
    try {
      const safeId = String(id);
      await postsApi.remove(safeId);
      myPosts = myPosts.filter(p => String(p.id) !== safeId);
      if (editingId === id) reset();
    } catch (e) {
      alert(e.data?.msg || "Failed to delete post.");
    }
  }
</script>

<div class="h-32"></div>

<section class="max-w-7xl mx-auto px-6 pb-20">
  {#if !$authStore.isLoggedIn}
    <div class="glass-panel p-20 text-center rounded-[3rem] text-white/50">
      Please log in to manage your articles.
    </div>
  {:else}
    <div class="grid grid-cols-1 lg:grid-cols-3 gap-12 items-start">
      
      <!-- WRITING INTERFACE -->
      <form class="lg:col-span-2 glass-panel p-10 rounded-[2.5rem] space-y-8" on:submit|preventDefault={save}>
        
        <div class="bg-blue-600/10 p-6 rounded-[2rem] border border-blue-500/20 flex items-center gap-4">
          <div class="bg-blue-600 p-3 rounded-xl text-xl">💡</div>
          <div>
            <p class="text-[9px] font-black text-blue-400 tracking-widest uppercase mb-1">Writing Tip</p>
            <p class="text-white text-sm italic">"{writingTip}"</p>
          </div>
        </div>

        <div class="flex justify-between items-end">
          <div>
            <p class="text-[10px] font-black text-blue-400 tracking-[0.3em] uppercase mb-2">Creator Studio</p>
            <h1 class="text-4xl font-black text-white uppercase tracking-tighter">
              {editingId ? 'Edit Article' : 'New Draft'}
            </h1>
          </div>
          {#if editingId}
            <button type="button" on:click={reset} class="text-white/30 hover:text-white text-xs font-bold uppercase transition-colors mb-1">
              Cancel Edit
            </button>
          {/if}
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
          <div class="space-y-2">
            <label class="text-[10px] text-white/40 font-black uppercase ml-1" for="article-title">Article Title</label>
            <input id="article-title" bind:value={title} placeholder="Enter a catchy title..." required class="form-input" />
          </div>
          <div class="space-y-2">
            <label class="text-[10px] text-white/40 font-black uppercase ml-1" for="category-select">Category</label>
            <select id="category-select" bind:value={category} class="form-input appearance-none">
              {#each CATEGORIES.filter(c => c !== 'All') as c}<option>{c}</option>{/each}
            </select>
          </div>
        </div>

        <div class="space-y-2">
          <label class="text-[10px] text-white/40 font-black uppercase ml-1" for="image-url">Banner Image URL</label>
          <input id="image-url" bind:value={imageUrl} placeholder="https://images.unsplash.com/..." class="form-input" />
        </div>

        <div class="space-y-2">
          <label class="text-[10px] text-white/40 font-black uppercase ml-1" for="summary">Brief Summary</label>
          <textarea id="summary" bind:value={description} placeholder="What is this article about?" rows="2" class="form-input"></textarea>
        </div>

        <!-- GitHub Repository Section -->
        <div class="space-y-2 bg-white/5 p-6 rounded-[2rem] border border-white/5 focus-within:border-blue-500/30 transition-all">
          <div class="flex items-center gap-3 mb-1">
            <div class="bg-white p-1.5 rounded-lg text-black">
              <svg height="16" viewBox="0 0 16 16" width="16" fill="currentColor"><path d="M8 0c4.42 0 8 3.58 8 8a8.013 8.013 0 0 1-5.45 7.59c-.4.08-.55-.17-.55-.38 0-.27.01-1.13.01-2.2 0-.75-.25-1.23-.54-1.48 1.78-.2 3.65-.88 3.65-3.95 0-.88-.31-1.59-.82-2.15.08-.2.36-1.02-.08-2.12 0 0-.67-.22-2.2.82-.64-.18-1.32-.27-2-.27-.68 0-1.36.09-2 .27-1.53-1.03-2.2-.82-2.2-.82-.44 1.1-.16 1.92-.08 2.12-.51.56-.82 1.28-.82 2.15 0 3.06 1.86 3.75 3.64 3.95-.23.2-.44.55-.51 1.07-.46.21-1.61.55-2.33-.66-.15-.24-.6-.83-1.23-.82-.67.01-.27.38.01.53.34.19.73.9.82 1.13.16.45.68 1.31 2.69.94 0 .67.01 1.3.01 1.49 0 .21-.15.45-.55.38A7.995 7.995 0 0 1 0 8c0-4.42 3.58-8 8-8Z"></path></svg>
            </div>
            <label class="text-[10px] text-white/40 font-black uppercase tracking-widest" for="github-repo">GitHub Repository (Optional)</label>
          </div>
          <input 
            id="github-repo" 
            bind:value={github_repo} 
            placeholder="e.g. sveltejs/svelte" 
            class="form-input !bg-transparent !border-none !p-0 !px-1 focus:ring-0" 
          />
          <p class="text-[9px] text-white/20 italic">The system will automatically fetch and store live repository stats.</p>
        </div>

        <div class="space-y-2">
          <label class="text-[10px] text-white/40 font-black uppercase ml-1">Full Content</label>
          <div class="editor-container">
            <div bind:this={editorElement}></div>
          </div>
        </div>

        {#if saveError}
          <p class="text-red-400 text-sm font-bold bg-red-500/10 p-4 rounded-xl border border-red-500/20">{saveError}</p>
        {/if}

        <button class="primary-submit-btn" disabled={saving}>
          {saving ? 'Processing...' : editingId ? 'Update Article' : 'Submit for Review'}
        </button>
      </form>

      <!-- ARCHIVE SIDEBAR -->
      <div class="glass-panel p-8 rounded-[2.5rem] space-y-6">
        <h2 class="text-xl font-bold text-white uppercase tracking-widest border-b border-white/10 pb-4 flex items-center gap-2">
          <span class="size-2 bg-blue-500 rounded-full"></span> My Archive
        </h2>
        
        <div class="space-y-4 max-h-[800px] overflow-y-auto pr-2 custom-scrollbar">
          {#each myPosts as post (post.id)}
            <div class="bg-white/5 p-5 rounded-2xl border border-white/5 hover:border-white/10 transition-all group">
              <div class="flex justify-between items-start mb-3">
                <span class="text-[9px] font-black uppercase px-2 py-1 rounded tracking-tighter
                  {post.status === 'Approved' ? 'bg-green-500/20 text-green-400' : 'bg-yellow-500/20 text-yellow-400'}">
                  {post.status || 'pending'}
                </span>
                <small class="text-white/20 text-[10px]">{formatDate(post.created_at)}</small>
              </div>
              <h3 class="text-white font-bold text-sm line-clamp-2 mb-4 group-hover:text-blue-400 transition-colors">
                {post.title}
              </h3>
              <div class="flex gap-2 opacity-60 group-hover:opacity-100 transition-opacity">
                <button class="action-btn bg-white/5 hover:bg-white/10" on:click={() => edit(post)}>Edit</button>
                <button class="action-btn bg-red-500/10 text-red-400 hover:bg-red-500 hover:text-white" on:click={() => remove(post.id)}>Delete</button>
              </div>
            </div>
          {:else}
            <p class="text-center text-white/20 italic py-10 text-sm">No articles found.</p>
          {/each}
        </div>
      </div>
    </div>
  {/if}
</section>

<style>
  @reference "../../app.css";

  .glass-panel { 
    background: rgba(15, 18, 25, 0.8); 
    backdrop-filter: blur(20px); 
    border: 1px solid rgba(255, 255, 255, 0.08); 
  }

  .form-input { 
    @apply w-full bg-white/5 border border-white/10 rounded-2xl px-5 py-3.5 text-white focus:border-blue-500/50 outline-none transition-all placeholder:text-white/10 text-sm; 
  }

  .editor-container { 
    @apply bg-white/5 border border-white/10 rounded-2xl overflow-hidden; 
  }

  .primary-submit-btn {
    @apply w-full py-4 bg-blue-600 hover:bg-blue-500 text-white rounded-2xl font-black uppercase tracking-widest text-xs transition-all shadow-lg shadow-blue-600/20 active:scale-[0.98] disabled:opacity-50;
  }

  .action-btn {
    @apply flex-1 py-2 rounded-xl text-[10px] font-black uppercase tracking-tighter transition-all;
  }

  /* Quill Dark Theme Overrides */
  :global(.ql-toolbar) { @apply !border-none !bg-white/5 !p-4; }
  :global(.ql-container) { @apply !border-none !text-white !text-sm; min-height: 300px; }
  :global(.ql-stroke) { stroke: rgba(255, 255, 255, 0.5) !important; }
  :global(.ql-fill) { fill: rgba(255, 255, 255, 0.5) !important; }
  :global(.ql-picker) { color: rgba(255, 255, 255, 0.5) !important; }
  :global(.ql-editor) { @apply !p-6; }
  :global(.ql-editor.ql-blank::before) { color: rgba(255, 255, 255, 0.1) !important; font-style: normal; }

  /* Custom Scrollbar */
  .custom-scrollbar::-webkit-scrollbar { width: 4px; }
  .custom-scrollbar::-webkit-scrollbar-track { background: transparent; }
  .custom-scrollbar::-webkit-scrollbar-thumb { background: rgba(255, 255, 255, 0.1); border-radius: 10px; }
</style>