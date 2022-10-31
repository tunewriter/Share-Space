<style>
	main {
		text-align: center;
		padding: 1em;
		max-width: 500px;
		margin: 0 auto;
	}

	.content {
	  	max-width: 500px;
	  	margin: auto;
		text-align: center;
	}

	h1 {
		font-size: 4em;
		font-weight: 300;
	}

    h2 {
		font-size: 2em;
		font-weight: 400;
        color: #aa8b56;
	}

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}

	:global(body) {
		background-color: #fffdfc;
		color: #000000;
		transition: background-color 0.3s
	}

	:global(body.dark-mode) {
		background-color: #395144;
		color: #fffdfc;
	}

	:global(button:hover:enabled){
    color: #fffdfc;
    background-color: #4E6C50;
    }

	:global(button){
    display:inline-block;
    padding:0.35em 1.2em;
    border:0.07em solid;
    margin:0 0.3em 0.3em 0;
    border-radius:0.12em;
    box-sizing: border-box;
    text-decoration:none;
    font-family:'Roboto',sans-serif;
    font-weight:300;
    text-align:center;
    transition: all 0.2s;
        background-color: #ffffff;
    }
</style>

<script>
	import Button from './Components/Button.svelte'
	import { Link, Route, navigate, Router } from 'svelte-routing';
	import Board from './Routes/+Board.svelte';
	import { writable } from 'svelte/store';
	import {login_state_wt, key_wt, server_url} from "./stores";
  	import { toast, SvelteToast } from '@zerodevx/svelte-toast'
	import Modal, {bind} from "svelte-simple-modal";
	import CreateCavePopup from "./Components/CreateCavePopup.svelte";
	import FooterBar from "./Components/FooterBar.svelte";

	document.body.style.setProperty('--text-color', '#4E6C50')

	let key_local ='';
	let logged = false
	let url = '';

	login_state_wt.subscribe(value => {
		logged = value;
	});

	server_url.subscribe(value => {
		url = value
	})

	// receive if key is true or false (String)
	async function check_key(){
		fetch(url + 'check/'+ key_local)
		.then((response) => response.json())
		.then((res) => {
			res = res['state']
			login_state_wt.set(eval(res))
			key_wt.set(key_local)
			if(logged) {
				toast.push("key is valid", {
			  		theme: {
						'--toastBackground': '#aa8b56',
						'--toastBarBackground': '#6c5937',
			  		},
					duration: 1800
				})
					// no toast here because there is a triggered toast in the page we're navigating
				navigate('/' + key_local, {replace: true});
			} else {
  				toast.push("key is not valid", {
  					theme: {
						'--toastBackground': '#cc4040',
						'--toastBarBackground': '#752424'
  					},
					duration: 1800
				})
			}
			key_local = ''
		})
	}

	const modalCreateCave = writable(null);
    const showCreateCave = () => modalCreateCave.set(CreateCavePopup);




</script>

<div style="display: flex;
	  justify-content: space-between;">
	<Button >☾</Button>
	<!-- show different things depending if logged -->
	{#if logged} <p style="font-style: italic"></p>
		{:else if logged === 0 }
			{:else } <p style="font-style: italic"></p>
	{/if}
</div>


<div class="content">
	<h1>
		<a href="http://www.syncave.com" style="text-decoration: none; color: #395144;">
			<p style="text-shadow: 5px 3px 2px #faf8f7;">Syncave</p>
		</a>
	</h1>
	{#if !logged}
		<h2 style="color: var(--text-color)">Access cave</h2>
		<form on:submit|preventDefault={() => check_key()}>
			<input class="key" type="password" bind:value={key_local} placeholder="Enter your key" autofocus>
			<button disabled={!key_local} type=submit>
				Enter
			</button>
		</form>

		<Modal
          show={$modalCreateCave}
          styleBg={{ backgroundColor: 'rgba(0,0,0,0.63)' }}
          styleWindow={{ boxShadow: '0 2px 5px 0 rgba(0, 0, 0, 0.15)' }}
          closeOnEsc=false
		  closeOnOuterClick=false
        >
          <button id="create_cave_button" on:click={showCreateCave}>Create new cave</button>
        </Modal>

	{/if}
</div>

<Router>
	<Route path="/:id" component="{Board}" />
</Router>

<SvelteToast></SvelteToast>

<FooterBar></FooterBar>