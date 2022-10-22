<script>
  import { CopyButton } from "carbon-components-svelte";
  import { toast, SvelteToast } from '@zerodevx/svelte-toast'
  import { Firework } from 'svelte-loading-spinners';


  let creator_name = '';
  let cave_name = '';
  let new_key = '';
  let created = false;
  let loading = false;

// create cave
    async function create_cave(creator_name, cave_name) {
        loading = true
        const res = await fetch('http://127.0.0.1:8000/createcave/', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({
                'creator_name': creator_name,
                'cave_name': cave_name
            })
        })
        const result = await res.json()
        created = true
        loading = false

        new_key = result["key"]

        toast.push("Cave created!", {
              theme: {
                '--toastBackground': '#693ee5',
                '--toastBarBackground': '#4a0f9f'
              }
            })
    }

    async function copytoast(){
        toast.push("Copied!", {
              theme: {
                '--toastBackground': '#3ea5e5',
                '--toastBarBackground': '#0d3256'
              },
            })
    }

</script>



{#if !created}
    {#if !loading}
        <form id="create_cave_form" on:submit|preventDefault={() => create_cave(creator_name, cave_name)}>
            <h3>Create new Cave</h3>
            <p><input type="text" bind:value={creator_name} placeholder="Your name" autofocus></p>
            <p><input type="text" bind:value={cave_name} placeholder="Cave Name"></p>
            <button disabled={!cave_name || !creator_name}> Enter </button>
        </form>
    {/if}
{/if}

{#if loading}
    <div style="position: absolute; left: 50%; transform: translateX(-50%); top: 40%">
        <Firework size="60" color="#FF3E00" unit="px" duration="1s" />
    </div>
    <div style="height: 155px"> </div>
{/if}

{#if created}
<form id="new_key_form">
    <h3>This is your new key</h3>
    <input type="text" bind:value={new_key} readonly>
    <CopyButton on:click={copytoast} text={new_key} feedback=""/>
</form>
{/if}


<SvelteToast></SvelteToast>