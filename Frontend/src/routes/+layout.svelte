<script>
    import favicon from '$lib/assets/favicon.svg';

    let { children } = $props();
</script>

<svelte:head>
    <link rel="icon" href={favicon} />
    <link
        href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap"
        rel="stylesheet"
    />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
</svelte:head>

<nav>
    <a href="/">Meus Cachorros</a>
    <a href="/cadastrar">+ Cadastrar</a>
</nav>

<main>
    {@render children()}
</main>

<style>
    :global(*) {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }

    :global(body) {
        font-family: 'Inter', system-ui, -apple-system, sans-serif;
        background: #f0f2f5;
        color: #1a1a2e;
        min-height: 100vh;
    }

    nav {
        background: #ffffff;
        padding: 1rem 2rem;
        display: flex;
        justify-content: space-between;
        align-items: center;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.08);
        position: sticky;
        top: 0;
        z-index: 10;
    }

    nav a {
        text-decoration: none;
        font-weight: 600;
        font-size: 0.95rem;
        color: #1a1a2e;
        padding: 0.5rem 1rem;
        border-radius: 8px;
        transition: background 0.2s;
    }

    nav a:last-child {
        background: #1a1a2e;
        color: white;
    }

    nav a:last-child:hover {
        background: #2d2d5e;
    }

    main {
        max-width: 1200px;
        margin: 0 auto;
        padding: 2rem;
    }
</style>
