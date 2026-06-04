<script>
    let dados = $state([]);

    async function receber() {
        const res = await fetch('http://127.0.0.1:8000/api/cachorros');
        dados = await res.json()
    }

    $effect(() => {
        receber()
    })
</script>

<ul class="container">
    {#each dados as item}
        <li class="cartaz">
            {item.id} - {item.nome} - {item.idade} - {item.raca} - {item.doenca}
        </li>
    {/each}
</ul>

<style>
    :global(body) {
        background-color: rgb(116, 160, 199);
    }
    .container {
        background-color: aqua;
    }
    .cartaz {
        background-color: green;
    }
</style>