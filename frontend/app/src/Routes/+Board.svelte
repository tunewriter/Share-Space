<style>
    .content {
	  	max-width: 500px;
	  	margin: auto;
		text-align: center;
	}
	:global(.card) {
		border: 1px solid black;
	}
    	button:hover:enabled{
    color:#000000;
    background-color: #ffffff;
    }
</style>

<script>
    import {login_state_wt, key_wt, board_name_wt} from "../stores";
    import {check_key} from "../checker";
    import Modal, { bind } from 'svelte-simple-modal';
    import { writable } from 'svelte/store';
    import Popup from "../Components/Popup.svelte";
    import {navigate} from "svelte-routing";
    import CollapsibleCard from '../Components/CollapsibleCard.svelte'
    import {onMount} from "svelte";



    let logged = false;
    let board_name = ""
    const url = window.location.href;

    let notes = []

    let local_key = url.split('/').at(-1)
    key_wt.set(local_key)
    check_key(local_key)

    login_state_wt.subscribe(value => {
		logged = value;
	});
    if (logged === false){
        navigate('/')
    }
    board_name_wt.subscribe(value => {
		board_name = value;
	});



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
        <h1 id="board_name">{board_name}</h1>

        <Modal
          show={$modal}
          styleBg={{ backgroundColor: 'rgba(120, 120, 120, 0.9)' }}
          styleWindow={{ boxShadow: '0 2px 5px 0 rgba(0, 0, 0, 0.15)' }}
          closeOnEsc=true
          closeOnOuterClick=true
        >
          <button id="add_note_button" on:click={showModal}>Add Note</button>
        </Modal>



            { #each notes as note } <!-- id, created, data -->
                <CollapsibleCard open={false} note_id={note.id} cave_key={local_key} >
                    <h3 slot='header'>{note.data}</h3>
                    <p slot='body' style="font-style: italic">created: {note.created}</p>
                </CollapsibleCard>
            { /each }

    {/if}

</div>