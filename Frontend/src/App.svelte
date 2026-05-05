<script>
  import { onMount } from 'svelte';
  import GlassyStars from './lib/components/GlassyStars.svelte';
  import Branding from './lib/components/Branding.svelte';
  import Navbar from './lib/components/Navbar.svelte';
  import Footer from './lib/components/Footer.svelte';
  
  // Routing views
  import HomeView from './routes/Main.svelte';
  import ReadPage from './routes/ReadPage.svelte';
  import About from './routes/About.svelte';
  import TopBlogs from './routes/TopBlogs.svelte';
  import Guidelines from './routes/Guidelines.svelte';
  
  // User views
  import Login from './routes/User/Login.svelte';
  import PostWrite from './routes/User/Posts.svelte';
  import LikedPosts from './routes/User/Likes.svelte';
  import SavedPosts from './routes/User/Later.svelte';
  import AccountManagement from './routes/User/Account.svelte';
  import AdminPanel from './routes/User/AdminPanel.svelte';

  // Import the 404 Component
  import NotFound from './routes/404.svelte';
  
  import LegalModal from './lib/components/LegalModal.svelte';
  import { authStore } from './lib/store.js';
  import { posts as postsApi } from './lib/api.js';

  let currentTab = 'Home';
  let currentModal = null;
  let selectedPost = null;
  let searchQuery = '';

  // Use the $ prefix for the store subscription in Svelte 4
  $: user = $authStore.user;
  $: isLoggedIn = $authStore.isLoggedIn;

  function handlePostClick(post) {
    selectedPost = post;
    currentTab = 'Read';
    // Smooth scroll to top when changing view
    window.scrollTo({ top: 0, behavior: 'smooth' });
    if (post?.id) history.replaceState(null, '', `#post-${post.id}`);
  }

  function logout() {
    // Corrected to use clearSession based on your store.js
    authStore.clearSession(); 
    currentTab = 'Home';
    selectedPost = null;
  }

  onMount(async () => {
    // Set initial theme for Tailwind
    const savedTheme = localStorage.getItem('theme') || 'dark';
    document.documentElement.dataset.theme = savedTheme;
    
    // Deep-linking logic for specific posts
    const match = location.hash.match(/post-(\d+)/);
    if (match) {
      try {
        const fetchedPost = await postsApi.get(match[1]);
        if (fetchedPost) {
            selectedPost = fetchedPost;
            currentTab = 'Read';
        } else {
            currentTab = '404';
        }
      } catch (err) {
        console.error("Failed to fetch linked post:", err);
        // Fallback to 404 if post fetch fails
        currentTab = '404';
      }
    }
  });
</script>

<!-- Global Background & Effects -->
<GlassyStars />
<Branding />

<!-- Modals & Navigation -->
<LegalModal bind:type={currentModal} />
<Navbar 
  bind:activeTab={currentTab} 
  onLogout={logout} 
  onSearch={(q) => searchQuery = q} 
/>

<!-- Main content area with tab-based routing -->
<main class="relative z-10 min-h-screen">
  {#if currentTab === 'Home'}
    <HomeView onPostClick={handlePostClick} {searchQuery} />
  {:else if currentTab === 'Read'}
    <ReadPage post={selectedPost} onPostClick={handlePostClick} />
  {:else if currentTab === 'About'}
    <About />
  {:else if currentTab === 'Top Blogs'}
    <TopBlogs onPostClick={handlePostClick} />
  {:else if currentTab === 'Guidelines'}
    <Guidelines />
  {:else if currentTab === 'Register/Log-in'}
    <Login onSuccess={() => currentTab = 'Home'} />
  {:else if currentTab === 'Write a Post'}
    <PostWrite onPostClick={handlePostClick} />
  {:else if currentTab === 'Liked Posts'}
    <LikedPosts onPostClick={handlePostClick} />
  {:else if currentTab === 'Saved Posts'}
    <SavedPosts onPostClick={handlePostClick} />
  {:else if currentTab === 'Account Settings'}
    <AccountManagement />
  {:else if currentTab === 'Admin Panel'}
    <AdminPanel onPostClick={handlePostClick} />
  {:else}
    <!-- This block handles 404 logic if currentTab doesn't match any of the above -->
    <NotFound />
  {/if}
</main>

<Footer bind:openModal={currentModal} />

<style>
  /* Base layout styles for Svelte 4 */
  :global(body) {
    margin: 0;
    padding: 0;
    overflow-x: hidden;
    background-color: var(--color-gemini-bg, #0B0E14); 
  }

  .app-shell {
    display: flex;
    flex-direction: column;
    min-height: 100vh;
  }
</style>