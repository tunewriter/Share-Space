<script>
  import { CopyButton } from "carbon-components-svelte";
  import { toast, SvelteToast } from '@zerodevx/svelte-toast'
  import { Firework } from 'svelte-loading-spinners';
  import {server_url} from "../stores";


  let creator_name = '';
  let cave_name = '';
  let new_key = '';
  let created = false;
  let loading = false;

  let url = '';

  server_url.subscribe(value => {
        url = value
    })

// create cave
    async function create_cave(creator_name, cave_name) {
        loading = true
        const res = await fetch(url + 'createcave/', {
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

        toast.push("Cave created with key: " + new_key, {
              theme: {
                '--toastBackground': '#4E6C50',
                '--toastBarBackground': '#304432',
              },
                duration: 20000
            })
    }

    const unsecuredCopyToClipboard = (text) => { const textArea = document.createElement("textarea"); textArea.value=text; document.body.appendChild(textArea); textArea.focus();textArea.select(); try{document.execCommand('copy')}catch(err){console.error('Unable to copy to clipboard',err)}document.body.removeChild(textArea)};

    const copyToClipboard = (content) => {
      if (window.isSecureContext && navigator.clipboard) {
        navigator.clipboard.writeText(content);
      } else {
        unsecuredCopyToClipboard(content);  // since we don't have https yet
      }
    };

    async function copytoast(){
        copyToClipboard(new_key)
        toast.push("Copied!", {
              theme: {
                '--toastBackground': '#513946',
                '--toastBarBackground': '#000000'
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
        <Firework size="60" color="#395144" unit="px" duration="1s" />
    </div>
    <div style="height: 155px"> </div>
{/if}

{#if created}
<form id="new_key_form">
    <h3>This is your new key</h3>
    <p> Take a screenshot or save it in case you lose it</p>
    <input type="text" bind:value={new_key} readonly>
    <CopyButton on:click={copytoast} text={new_key} feedback=""/>
    <p> Access your cave through: </p> <a href={"http://www.syncave.com/"+new_key}>{"syncave.com/"+new_key}</a>
</form>
{/if}


<SvelteToast></SvelteToast>