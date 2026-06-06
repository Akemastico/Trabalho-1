<script>
    let dados = $state([]);
    let carregando = $state(true);

    async function receber() {
        carregando = true;
        const res = await fetch('http://127.0.0.1:8000/api/cachorros');
        dados = await res.json();
        carregando = false;
    }

    $effect(() => {
        receber();
    });
</script>

<h1>Meus Cachorros</h1>

{#if carregando}
    <p class="vazio">Carregando...</p>
{:else if dados.length === 0}
    <div class="vazio">
        <p>Nenhum cachorro cadastrado ainda.</p>
        <a href="/cadastrar" class="btn">Cadastrar primeiro cachorro</a>
    </div>
{:else}
    <div class="grid">
        {#each dados as item}
            <div class="cartaz">
                <div class="foto-wrapper">
                    {#if item.imagem}
                        <img src={item.imagem} alt={item.nome} />
                    {:else}
                        <div class="sem-foto">Sem foto</div>
                    {/if}
                </div>
                <div class="info">
                    <h2>{item.nome}</h2>
                    <div class="detalhes">
                        <span class="tag">Raça: {item.raca}</span>
                        <span class="tag">{item.idade} {item.idade === 1 ? 'ano' : 'anos'}</span>
                    </div>
                    <p class="doenca">{item.doenca}</p>
                </div>
            </div>
        {/each}
    </div>
{/if}

<style>
    h1 {
        font-size: 1.8rem;
        font-weight: 700;
        margin-bottom: 1.5rem;
        color: #1a1a2e;
    }

    .vazio {
        text-align: center;
        margin-top: 4rem;
        color: #666;
        font-size: 1.1rem;
    }

    .btn {
        display: inline-block;
        margin-top: 1rem;
        padding: 0.75rem 1.5rem;
        background: #1a1a2e;
        color: white;
        text-decoration: none;
        border-radius: 10px;
        font-weight: 600;
        font-size: 0.95rem;
        transition: background 0.2s;
    }

    .btn:hover {
        background: #2d2d5e;
    }

    .grid {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
        gap: 1.5rem;
    }

    .cartaz {
        background: white;
        border-radius: 16px;
        overflow: hidden;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
        transition: transform 0.2s, box-shadow 0.2s;
    }

    .cartaz:hover {
        transform: translateY(-4px);
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.1);
    }

    .foto-wrapper {
        width: 100%;
        aspect-ratio: 4 / 3;
        overflow: hidden;
        background: #e0e0e0;
    }

    .foto-wrapper img {
        width: 100%;
        height: 100%;
        object-fit: cover;
        display: block;
    }

    .sem-foto {
        width: 100%;
        height: 100%;
        display: flex;
        align-items: center;
        justify-content: center;
        color: #999;
        font-size: 0.9rem;
    }

    .info {
        padding: 1.25rem;
    }

    .info h2 {
        font-size: 1.25rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
        color: #1a1a2e;
    }

    .detalhes {
        display: flex;
        flex-wrap: wrap;
        gap: 0.5rem;
        margin-bottom: 0.5rem;
    }

    .tag {
        font-size: 0.8rem;
        background: #f0f2f5;
        color: #555;
        padding: 0.25rem 0.75rem;
        border-radius: 20px;
        font-weight: 500;
    }

    .doenca {
        font-size: 0.85rem;
        color: #888;
        margin-top: 0.25rem;
    }
</style>
