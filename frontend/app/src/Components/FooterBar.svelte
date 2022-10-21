<style>
    #footer{
    display:block;
    position:absolute;
    left:0;
    right:0;
    bottom:0;
    padding-top: 14px;
    padding-bottom: 14px;
    padding-left: 24px;
    height: 36px;
    text-align: center;
    }

    .button{
    display:inline-block;
    padding:0.35em 1.2em;
    border:0.1em solid #000000;
    margin:0 0.3em 0.3em 0;
    border-radius:0.12em;
    box-sizing: border-box;
    text-decoration:none;
    font-family:'Roboto',sans-serif;
    font-weight:300;
    color: #000000;
    text-align:center;
    transition: all 0.2s;
        background-color: white;
    }
    .button:hover{
    color:#000000;
    background-color: #fff7ed;
    }
</style>

<script>
  import {writable} from "svelte/store";
  import FeedbackPopup from "./FeedbackPopup.svelte";
  import Modal, {bind} from "svelte-simple-modal";

  const modalFeedback = writable(null);
  const showFeedback = () => modalFeedback.set(FeedbackPopup);
</script>



<div id="footer">
    <Modal
      show={$modalFeedback}
      styleBg={{ backgroundColor: 'rgba(120, 120, 120, 0.9)' }}
      styleWindow={{ boxShadow: '0 2px 5px 0 rgba(0, 0, 0, 0.15)' }}
      closeOnEsc=true
    >
        <div style="padding-right: 50px">
            <button class="button" style="float: right;" on:click={showFeedback}> Which Feature would you like?</button>
        </div>
    </Modal>
</div>