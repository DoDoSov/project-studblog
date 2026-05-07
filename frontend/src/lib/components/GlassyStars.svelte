<script>
  // Stars generation logic (stays the same)
  const rows = 12;
  const cols = 7;
  const spawnChance = 0.25;
  const grid = [];
  
  for (let r = 0; r < rows; r++) {
    for (let c = 0; c < cols; c++) {
      if (Math.random() < spawnChance) {
        grid.push({
          top: (r * (100 / rows)) + (Math.random() * 4),
          left: (c * (100 / cols)) + (Math.random() * 4),
          delay: Math.random() * -10,
          duration: 6 + Math.random() * 6,
          size: 15 + Math.random() * 30,
          rotation: Math.random() * 360
        });
      }
    }
  }
</script>

<svg style="position: absolute; width: 0; height: 0; pointer-events: none;" aria-hidden="true">
  <defs>
    <radialGradient id="geminiGradient">
      <stop offset="0%" stop-color="#FFF" />
      <stop offset="40%" stop-color="#A78BFA" /> 
      <stop offset="100%" stop-color="#3B82F6" />
    </radialGradient>
    <filter id="geminiGlow">
      <feGaussianBlur stdDeviation="3" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
  </defs>
</svg>

<div class="stars-container">
  {#each grid as star}
    <div 
      class="star-wrapper"
      style="
        top: {star.top}%; 
        left: {star.left}%; 
        --delay: {star.delay}s; 
        --duration: {star.duration}s;
        --size: {star.size}px;
        --init-rot: {star.rotation}deg;
      "
    >
      <svg viewBox="0 0 100 100" class="star-svg">
        <path 
          d="M50 0C50 27.6 72.4 50 100 50C72.4 50 50 72.4 50 100C50 72.4 27.6 50 0 50C27.6 50 50 27.6 50 0Z" 
          fill="url(#geminiGradient)"
          filter="url(#geminiGlow)"
        />
        <circle cx="50" cy="50" r="10" fill="white" filter="url(#geminiGlow)" />
      </svg>
    </div>
  {/each}
</div>

<style>
  .stars-container {
    position: fixed;
    inset: 0;
    width: 100%;
    height: 100%;
    z-index: -50;
    overflow: hidden;
    pointer-events: none;
    perspective: 1000px;
    transition: background 1s ease-in-out; /* Smooth color transition */
    
    /* DEFAULT DARK THEME GRADIENT */
    background: radial-gradient(circle at 50% 50%, #111827 0%, #0B0E14 100%);
  }

  /* Listen for theme changes on the :root but apply it here */
  :global(:root[data-theme='warm']) .stars-container {
    background: radial-gradient(circle at 50% 50%, #452727 0%, #1a0f0f 100%);
  }

  :global(:root[data-theme='contrast']) .stars-container {
    background: #000000;
  }

  .star-wrapper {
    position: absolute;
    width: var(--size);
    height: var(--size);
    will-change: transform;
    animation: float-3d var(--duration) ease-in-out infinite alternate;
    animation-delay: var(--delay);
    filter: drop-shadow(0 0 10px rgba(167, 139, 250, 0.4));
  }

  .star-svg {
    width: 100%;
    height: 100%;
    will-change: opacity, transform;
    animation: twinkle var(--duration) ease-in-out infinite;
    animation-delay: var(--delay);
  }

  @keyframes float-3d {
    0% { transform: translateZ(0) translateY(0) rotate(var(--init-rot)); }
    100% { transform: translateZ(60px) translateY(-40px) rotate(calc(var(--init-rot) + 20deg)); }
  }

  @keyframes twinkle {
    0%, 100% { opacity: 0.2; transform: scale(0.8); }
    50% { opacity: 1; transform: scale(1.1); }
  }
</style>