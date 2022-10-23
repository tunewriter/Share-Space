describe('Send feedback', () => {
    beforeEach(() => {
        cy.visit('http://localhost:3400/')
        cy.get("#feedback-button").click()      // Click Feedback button
        cy.get("#feedback_form > h3").should("contain", "Enter Feedback")   // Check Popup text
    })


    it('Enter only text', () => {
        cy.get("#feedback_form > p:nth-child(3) > textarea")
            .type("cypress test feedback")
    })

    it('Enter text and email', () => {
        cy.get("#feedback_form > p:nth-child(3) > textarea")
            .type("cypress test feedback")
        cy.get("#feedback_form > p:nth-child(2) > input[type=text]")
            .type("safsfasfsf@gmail.com")
    })

    it('Enter long text', () => {
        cy.get("#feedback_form > p:nth-child(3) > textarea")
            .type("cypress test feedback: " + 'a'.repeat(5000), {delay: 0})
    })

    afterEach(()=>{     // always send and check toast
        cy.get("#feedback_form")
            .submit()
        cy.get("body > ul > li > div > div._toastMsg.svelte-10l0ogd")
            .should("contain", "Thanks for your Feedback!")
    })
})
