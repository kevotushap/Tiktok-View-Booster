import pystyle


class UI:
    def banner(self):
        banner_text = """
        ************************************
        *           Tiktok-View-Booster            *
        ************************************
        """
        # Debug: Print pystyle attributes
        print("pystyle attributes:", dir(pystyle))
        print("pystyle.Center:", pystyle.Center)

        # Alternative method to center text if pystyle.Center is None
        width = 80  # Adjust the width as needed
        lines = banner_text.split('\n')
        centered_lines = [line.center(width) for line in lines]
        centered_banner = '\n'.join(centered_lines)

        print(centered_banner)
