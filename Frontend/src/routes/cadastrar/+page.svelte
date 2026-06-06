<script>
    import { goto } from '$app/navigation';

    let nome = $state('');
    let idade = $state('');
    let raca = $state('');
    let doenca = $state('');
    let enviando = $state(false);
    let sucesso = $state(false);

    async function enviar(evento) {
        evento.preventDefault();
        enviando = true;

        const fd = new FormData();
        fd.append('nomec', nome);
        fd.append('idadec', idade);

        if (!raca) {
            fd.append('raca', 'Vira Lata');
        } else {
            fd.append('raca', raca);
        }

        if (!doenca) {
            fd.append('doenca', 'Não Há Doenças');
        } else {
            fd.append('doenca', doenca);
        }

        const res = await fetch('http://127.0.0.1:8000/api/cadastrar', {
            method: 'POST',
            body: fd
        });

        enviando = false;

        if (res.ok) {
            sucesso = true;
            setTimeout(() => goto('/'), 1500);
        }
    }
</script>

<div class="container">
    <h1>Cadastrar Cachorro</h1>

    <form onsubmit={enviar}>
        <label>
            Nome
            <input required bind:value={nome} placeholder="ex: Rex" />
        </label>

        <label>
            Idade
            <input type="number" min="1" required bind:value={idade} placeholder="ex: 3" />
        </label>

        <label>
            Raça
            <input bind:value={raca} placeholder="Vira Lata (padrão)" />
        </label>

        <label>
            Doença
            <input bind:value={doenca} placeholder="Nenhuma (opcional)" />
        </label>

        <button type="submit" disabled={enviando}>
            {enviando ? 'Cadastrando...' : 'Cadastrar'}
        </button>
    </form>

    {#if sucesso}
        <div class="toast">Cadastrado com sucesso! Redirecionando...</div>
    {/if}
</div>

<style>
    .container {
        max-width: 480px;
        margin: 0 auto;
    }

    h1 {
        font-size: 1.8rem;
        font-weight: 700;
        margin-bottom: 1.5rem;
        color: #1a1a2e;
    }

    form {
        display: flex;
        flex-direction: column;
        gap: 1rem;
    }

    label {
        display: flex;
        flex-direction: column;
        gap: 0.3rem;
        font-size: 0.85rem;
        font-weight: 600;
        color: #444;
    }

    input {
        padding: 0.75rem 1rem;
        border: 1.5px solid #ddd;
        border-radius: 10px;
        font-size: 0.95rem;
        font-family: inherit;
        transition: border-color 0.2s;
        outline: none;
    }

    input:focus {
        border-color: #1a1a2e;
    }

    button {
        margin-top: 0.5rem;
        padding: 0.85rem;
        background: #1a1a2e;
        color: white;
        border: none;
        border-radius: 10px;
        font-size: 1rem;
        font-weight: 600;
        cursor: pointer;
        transition: background 0.2s;
    }

    button:hover:not(:disabled) {
        background: #2d2d5e;
    }

    button:disabled {
        opacity: 0.6;
        cursor: not-allowed;
    }

    .toast {
        margin-top: 1rem;
        padding: 0.75rem 1rem;
        background: #d4edda;
        color: #155724;
        border-radius: 10px;
        font-size: 0.9rem;
        font-weight: 500;
        text-align: center;
    }
</style>
