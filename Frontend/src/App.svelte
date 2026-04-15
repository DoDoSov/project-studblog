<script>
  import Branding from './lib/components/Branding.svelte';
  import Navbar from './lib/components/Navbar.svelte';
  import Footer from './lib/components/Footer.svelte';
  import Category from './lib/components/Category.svelte';
  import PostCard from './lib/components/PostCard.svelte';

  const trendingPosts = [
    {
      title: "Getting Started with JavaScript in 2026",
      description: "A beginner-friendly guide to understanding the basics of JavaScript and building your first interactive page.",
      image: "https://picsum.photos/seed/js/600/400",
      tags: ["JavaScript", "WebDev", "Beginner"]
    },
    {
      title: "Why React Still Dominates Frontend Development",
      description: "An overview of why React remains the most popular choice for modern web apps.",
      image: "https://picsum.photos/seed/react/600/400",
      tags: ["React", "Frontend", "Career"]
    },
    {
      title: "Understanding REST APIs with Real Examples",
      description: "Learn how REST APIs work and how to use them in your projects with clear, real-world scenarios.",
      image: "https://picsum.photos/seed/api/600/400",
      tags: ["API", "Backend", "Logic"]
    }
  ];
  const latestPosts = [
    {
      title: "The Future of AI in Web Design",
      description: "How generative tools are changing the way we think about user interfaces.",
      image: "https://picsum.photos/seed/ai-web/600/400",
      tags: ["AI", "Design", "2026"]
    },
    {
      title: "Mastering Tailwind v4",
      description: "Everything you need to know about the new CSS-first engine.",
      image: "https://picsum.photos/seed/tailwind/600/400",
      tags: ["CSS", "Tailwind", "Frontend"]
    },
    {
      title: "10 Tips for Remote Developers",
      description: "Staying productive and healthy while working from anywhere in the world.",
      image: "https://picsum.photos/seed/remote/600/400",
      tags: ["Lifestyle", "Career"]
    }
  ];
</script>


<Branding />
<div class="flex flex-col min-h-screen bg-brand-dark text-white">
  
  <Navbar />
  <Category />
  <section class="m-4 bg-[#2D364F]/30 p-6 rounded-3xl border border-white/5">
  <div class="flex justify-between items-center mb-6">
    <h2 class="text-xl font-bold text-white px-4 py-1 bg-white/5 rounded-lg">Trending</h2>
  </div>

  <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
    {#each trendingPosts as post}
      <PostCard {...post} />
    {/each}
  </div>
  </section>
  <section class="mx-4 mb-10 bg-brand-card/10 p-6 rounded-3xl border border-white/5">
  <div class="flex justify-between items-center mb-6">
    <h2 class="text-xl font-bold text-white px-4 py-1 bg-white/5 rounded-lg">Latest</h2>
  </div>

  <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
    {#each latestPosts as post}
      <PostCard {...post} />
    {/each}
  </div>

 
</section>
  <main class="flex-grow p-8">
    <h1 class="text-4xl font-bold text-center">Trending Content will go here...</h1>
    
    </main>

  <Footer />
</div>

<style lang="postcss">
  @reference "tailwindcss";
  :global(html) {
    
  }
</style>