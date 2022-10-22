<script>
  import { toast, SvelteToast } from '@zerodevx/svelte-toast'
  import { Firework } from 'svelte-loading-spinners';


  let email = '';
  let feedback = '';
  let loading = false;

// send feedback
    async function send_feedback(email, text) {
        loading = true
        const res = await fetch('http://127.0.0.1:8000/feedback/', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({
                'email': email,
                'text': text
            })
        })
        const result = await res.json()
                    loading = false
        if (result['ok']) {
            toast.push("Thanks for your Feedback!", {
                theme: {
                    '--toastBackground': '#693ee5',
                    '--toastBarBackground': '#4a0f9f'
                }
            })
        } else {
            toast.push("Feedback could not be send!", {
                theme: {
                    '--toastBackground': '#be4b4b',
                    '--toastBarBackground': '#621f1f'
                }
            })
        }
    }

</script>





    {#if !loading}
        <form id="feedback_form" on:submit|preventDefault={() => send_feedback(email, feedback)}>
            <h3>Enter Feedback</h3>
            <p>
                <input type="text" bind:value={email} placeholder="Email (Optional)">
            </p>
            <p>
                <textarea bind:value={feedback} maxlength="5000" placeholder="It would be cool if.." autofocus></textarea>
            </p>
            <button disabled={!feedback}> Enter </button>
        </form>
    {/if}


{#if loading}
    <div style="position: absolute; left: 50%; transform: translateX(-50%); top: 40%">
        <Firework size="60" color="#FF3E00" unit="px" duration="1s" />
    </div>
    <div style="height: 155px"> </div>
{/if}


<SvelteToast></SvelteToast>