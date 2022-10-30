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
        color: #f76027;
	}

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}

	:global(body) {
		background-color: #ffffff;
		color: #000000;
		transition: background-color 0.3s
	}

	:global(body.dark-mode) {
		background-color: rgba(1, 16, 28, 0.99);
		color: #ffffff;
	}

	button:hover:enabled{
    color:#000000;
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
						'--toastBackground': '#3a9463',
						'--toastBarBackground': '#246545',
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
	<h1><a href="http://www.syncave.com" style="text-decoration: none; color: black">Syncave</a></h1>
	{#if !logged}
		<h2>Access cave</h2>
		<form on:submit|preventDefault={() => check_key()}>
			<input class="key" type="password" bind:value={key_local} placeholder="Enter your key" autofocus>
			<button disabled={!key_local} type=submit>
				Enter
			</button>
		</form>

		<Modal
          show={$modalCreateCave}
          styleBg={{ backgroundColor: 'rgba(120, 120, 120, 0.9)' }}
          styleWindow={{ boxShadow: '0 2px 5px 0 rgba(0, 0, 0, 0.15)' }}
          closeOnEsc=true
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