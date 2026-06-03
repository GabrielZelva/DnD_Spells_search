from shiny import App, render, ui
from functionality import db, IR

app_ui = ui.page_sidebar(
    ui.sidebar(
        ui.input_text_area("query", "Describe the spell you want", "I need to hit my enemies with a lot of ice!"),
        ui.input_slider("k", "How many spells do you want to show?", 0, 20, 3),
        ui.markdown("""
                    [GitHub repository](https://github.com/GabrielZelva/DnD_Spells_search)
                    """),
    ),
    ui.output_ui("text"),
    title= ui.markdown("""
                       # **DnD e5 Spell Search**
                       *Describe what you want to do and see if there is a spell for it!*
                       """),
)

def server(input, output, session):
    @render.ui
    def text():
        result = IR(db, input.query(), input.k())
        return ui.markdown(result)

app = App(app_ui, server)

if __name__ == "__main__":
    app.run()
