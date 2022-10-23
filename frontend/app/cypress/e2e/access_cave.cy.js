const urls = ['http://localhost:8080/', 'http://localhost:8080/abcd']

urls.forEach((url)=>{   // once with login through homepage, once login through url

  describe('Access Cave through ' + url, () => {
    beforeEach(()=>{
      cy.visit(url, { timeout: 90000 })
      if(url === 'http://localhost:8080/'){   // if not logged, entry login key
        cy.get('.key').type('abcd')
        cy.get('form').submit()
      }
    })

    it('Access Cave and check board title', () => {
      cy.get("#board_name").should("contain", "Test Cave")
    })

    it('Access Cave and adding note', () => {
      cy.get("#add_note_button").click()  // click on 'add note'
      cy.get("#add_note_form > input[type=text]")
          .type("cypress test")
      cy.get("#add_note_form")
          .submit()
    })

    it('Access Cave and read created note', () => {
      cy.get("#note_card > h3")
          .should("contain", "cypress test")
    })

    it('Access Cave and delete created note', () => {
      cy.get("#note_card > h3")
          .should("contain", "cypress test")  // check if it deletes the right note
      cy.get("#note_card")
          .click()  // open card
      cy.get("#delete_note_button")
          .click()  // delete note
      cy.get("body > ul > li > div > div._toastMsg.svelte-10l0ogd")
          .should('contain', 'Note was deleted!')   // check if toast is correct
    })

    it('Access Cave through URL', () => {
      cy.visit('http://localhost:8080/abcd')
    })
  })
})


