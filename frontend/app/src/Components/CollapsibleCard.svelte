<script>
    import { createEventDispatcher } from 'svelte'
    import collapse from 'svelte-collapse'
    import {toast} from "@zerodevx/svelte-toast";
    import {server_url} from "../stores";
    import { CopyButton } from "carbon-components-svelte";

    export let open = true
    export let duration = 0.2
    export let easing = 'ease'
    export let note_id;
    export let cave_key;
    export let note_text;

    let url = '';

    server_url.subscribe(value => {
		url = value
	})

    const dispatch = createEventDispatcher()

    function handleToggle () {

        open = !open

        if (open) {
            dispatch('open')
        }
        else {
            dispatch('close')
        }

    }

    async function delete_note (key, id) {
        await fetch(url + 'delete_note/' + key + '/' + id, {
            method: 'DELETE',
            headers: {'Content-Type': 'application/json'}
        })
        .then(res => {
            if (res.ok) {
                console.log("HTTP request successful")
                /*toast.push("Note was deleted!", {
                  theme: {
                    '--toastBackground': '#be4b4b',
                    '--toastBarBackground': '#621f1f'
                  }
                })
                 */
                location.reload();
            }
            else {
                console.log("HTTP request unsuccessful")
            }
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
        copyToClipboard(note_text)
        toast.push("Copied!", {
              theme: {
                '--toastBackground': '#513946',
                '--toastBarBackground': '#000000'
              },
            duration: 750
            })
    }

</script>

<div class='card' class:open aria-expanded={open}>

    <div class='card-header' id="note_card" on:click={handleToggle}>
        <slot name='header'/>
    </div>

    <div class='card-body' use:collapse={{open, duration, easing}}>
        <slot name='body'/>
        <span on:pointerdown={e => e.stopPropagation()}
              on:click={() => delete_note(cave_key, note_id)}
              class=remove
              id="delete_note_button"
        >
            delete
        </span>
        <CopyButton on:click={copytoast} feedback=""/>
    </div>

</div>

<style>

    .card-header {
        cursor: pointer;
        user-select: none;
    }

    .remove {
	cursor: pointer;
	right: 5px;
	top: 3px;
	user-select: none;
    color: palevioletred;
}

</style>