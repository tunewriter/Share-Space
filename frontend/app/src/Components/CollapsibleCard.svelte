<script>
    import { createEventDispatcher } from 'svelte'
    import collapse from 'svelte-collapse'
    import {toast} from "@zerodevx/svelte-toast";

    export let open = true
    export let duration = 0.2
    export let easing = 'ease'
    export let note_id;
    export let cave_key;

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
        await fetch('http://127.0.0.1:8000/delete_note/' + key + '/' + id, {
            method: 'DELETE',
            headers: {'Content-Type': 'application/json'}
        })
        .then(res => {
            if (res.ok) {
                console.log("HTTP request successful")
                toast.push("Note was deleted!", {
                  theme: {
                    '--toastBackground': '#be4b4b',
                    '--toastBarBackground': '#621f1f'
                  }
                })
            }
            else {
                console.log("HTTP request unsuccessful")
            }
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