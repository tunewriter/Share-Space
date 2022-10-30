describe('Create Cave', () => {
    beforeEach(() => {
        cy.visit('http://localhost:8080/')
        cy.get("#create_cave_button").click()      // Click Feedback button
        cy.get("#create_cave_form > h3").should("contain", "Create new Cave")   // Check Popup text
    })

    it('Enter name and cave name', () => {
        cy.get("#create_cave_form > p:nth-child(2) > input[type=text]")
            .type("joe")
        cy.get("#create_cave_form > p:nth-child(3) > input[type=text]")
            .type("cypress test cave")
    })

    afterEach(()=>{
        cy.get("#create_cave_form")
            .submit()
        cy.get("body > ul > li > div > div._toastMsg.svelte-10l0ogd")
            .should("contain", "Cave created with key")
        cy.get("#new_key_form > h3")
            .should("contain", "This is your new key")
        cy.get("#new_key_form > button")
            .click()
        cy.window().then((win) => {     // check new key not to be empty (copied from clipboard)
            win.navigator.clipboard.readText().then((text) => {
              expect(text).not.empty
             });
        });
    })
})