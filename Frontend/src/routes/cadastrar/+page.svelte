<script>
    let nome = $state();
    let idade = $state();
    let raca = $state();
    let doenca = $state();

    async function enviar(evento) {
        evento.preventDefault();
        const fd = new FormData();
        fd.append("nomec", nome)
        fd.append("idadec", idade)

        if (!raca) {
            fd.append('raca', 'Vira Lata')
        } else {
            fd.append('raca', raca)
        }

        if (!doenca) {
            fd.append('doenca', 'Não Há Doenças')
        } else {
            fd.append('doenca', doenca)
        }

        const res = await fetch('http://127.0.0.1:8000/api/cadastrar', {
            method: 'POST',
            body: fd
        })

        if (res.ok) {
            console.log('Cadastrado com sucesso')
        }
    }
</script>

<form method="POST" id="formulario" onsubmit={enviar}>
    <input class="input" required bind:value={nome} placeholder="Nome" />
    <input class="input" type="number" min="1" bind:value={idade} placeholder="Idade" />
    <input class="input" bind:value={raca} placeholder="Raca(Null= Vira Lata)"/>
    <input class="input" bind:value={doenca} placeholder="Doença (opcional)" />
    <button type="submit"> Clique Aqui Para Enviar</button>
</form>

<style>
    .input {
        margin: 10px;
        width: 70%;
    }
    #formulario {
        display: flex;
        flex-direction: column;
        width: 50vw;
        background-color: aliceblue;
        border: 1px black solid;
        border-radius: 10px;
        align-items: center;
    }
</style>
