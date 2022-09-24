<style>
    .content {
	  	max-width: 500px;
	  	margin: auto;
		text-align: center;
	}
	:global(.card) {
		border: 1px solid black;
	}
</style>

<script>
    import {login_state, key} from "../stores";
    import {check_key} from "../checker";
    import Modal, { bind } from 'svelte-simple-modal';
    import { writable } from 'svelte/store';
    import Popup from "../Components/Popup.svelte";
    import {navigate} from "svelte-routing";
    import { CollapsibleCard } from 'svelte-collapsible'
    import {onMount} from "svelte";



    let logged = false;
    const url = window.location.href;

    let notes = []

    let local_key = url.split('/').at(-1)
    check_key(local_key)
    login_state.subscribe(value => {
		logged = value;
	});
    if (logged === false){
        navigate('/')
    }
    key.set(local_key)
    const modal = writable(null);
    const showModal = () => modal.set(bind(Popup, { message: 'Enter your note' }));


    function load_notes(key){
        onMount(async () => {
        const response = await fetch('http://127.0.0.1:8000/notes/'+key);
        const res = await response.json();
		notes = eval(res[0])
        notes = notes.reverse() // newest item on top
    })
    }

    load_notes(local_key)


</script>

<div class="content">
    {#if logged}
        <h1>Board</h1>

        <Modal
          show={$modal}
          styleBg={{ backgroundColor: 'rgba(120, 120, 120, 0.9)' }}
          styleWindow={{ boxShadow: '0 2px 5px 0 rgba(0, 0, 0, 0.15)' }}
          closeOnEsc=true
          closeOnOuterClick=true
        >
          <button on:click={showModal}>Add Note</button>
        </Modal>



            { #each notes as note } <!-- id, created, data -->
                <CollapsibleCard open={false}>
                    <h3 slot='header'>{note.data}</h3>
                    <p slot='body' style="font-style: italic">created: {note.created}</p>
                </CollapsibleCard>
            { /each }

    {/if}

</div>