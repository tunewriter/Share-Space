<script>
function toggle() {
	window.document.body.classList.toggle('dark-mode')
	if(document.body.style.getPropertyValue('--text-color') === '#aa8b56'){
		document.body.style.setProperty('--text-color', '#4E6C50')
	} else {
		document.body.style.setProperty('--text-color', '#aa8b56')
	}
}
</script>
<button on:click={toggle}>
	<slot/>
</button>
<style>
	button {
		background-color: #395144;
		color: #F0EBCE;
		border: none;
		border-radius: 4px;
		padding: 0.5rem;
		text-transform: uppercase;
	}
	:global(body.dark-mode) button {
		background-color: #aa8b56;
		color: #F0EBCE;
	}
</style>