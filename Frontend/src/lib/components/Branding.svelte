<script>
  /**
   * Svelte 4 Script Block
   * Standard variable declarations are reactive by default when updated.
   */
  import IconLogo from '../../assets/Website/logo.svg';
  
  let title = "StudPlace";
</script>

<svelte:head>
  <!-- Dynamically sets the browser tab title -->
  <title>{title}</title>
  
  <!-- Injects the favicon into the document head -->
  <link rel="icon" type="image/svg+xml" href="{IconLogo}" /> 
  
  <!-- Ensures proper scaling across mobile and desktop devices -->
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
</svelte:head>