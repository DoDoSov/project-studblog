<script>
  import GlassyStars from './lib/components/GlassyStars.svelte';
  import Branding from './lib/components/Branding.svelte';
  import Navbar from './lib/components/Navbar.svelte';
  import Footer from './lib/components/Footer.svelte';

  import HomeView from './routes/Main.svelte';
  import ReadPage from './routes/ReadPage.svelte';
  import About from './routes/About.svelte';
  import TopBlogs from './routes/TopBlogs.svelte';
  import Guidelines from './routes/Guidelines.svelte';

  import AccountManagement from './routes/User/Account.svelte';
  import LikedPosts from './routes/User/Likes.svelte';
  import SavedPosts from './routes/User/Later.svelte';
  import PostWrite from './routes/User/Posts.svelte';
  import AdminPanel from './routes/User/Management.svelte';
  import Login from './routes/User/Login.svelte';

  import LegalModal from './lib/components/LegalModal.svelte';
  import { authStore } from './lib/store.js';

  let currentTab   = 'Home';
  let currentModal = null;
  let selectedPost = null;

  function handlePostClick(post) {
    selectedPost = post;
    currentTab   = 'Read';
  }

  function handleLoginSuccess(user) {
    currentTab = 'Home';
  }

  function handleLogout() {
    authStore.clearSession();
    currentTab = 'Home';
  }
</script>

<Branding />
<GlassyStars />
<LegalModal bind:type={currentModal} />
<Navbar
  bind:activeTab={currentTab}
  isLoggedIn={authStore.isLoggedIn}
  userRole={authStore.user?.role}
  onLogout={handleLogout}
/>

<main>
  {#if currentTab === 'Home'}
    <HomeView onPostClick={handlePostClick} />
  {:else if currentTab === 'Read'}
    <ReadPage post={selectedPost} />
  {:else if currentTab === 'About'}
    <About />
  {:else if currentTab === 'Top Blogs'}
    <TopBlogs />
  {:else if currentTab === 'Guidelines'}
    <Guidelines />
  {:else if currentTab === 'Register/Log-in'}
    <Login onSuccess={handleLoginSuccess} />
  {:else if currentTab === 'Write a Post'}
    <PostWrite />
  {:else if currentTab === 'Liked Posts'}
    <LikedPosts />
  {:else if currentTab === 'Saved Posts'}
    <SavedPosts />
  {:else if currentTab === 'Account Settings'}
    <AccountManagement />
  {:else if currentTab === 'Management Panel'}
    <AdminPanel />
  {:else}
    <div class="h-screen flex items-center justify-center text-white/20 uppercase tracking-widest">
      {currentTab} Section Coming Soon
    </div>
  {/if}
</main>

<Footer bind:openModal={currentModal} />

<style lang="postcss">
  @reference "tailwindcss";
</style>
