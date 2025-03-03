from config.gan import GAN


class GanUtil:
    @staticmethod
    def find_interaction(guest_can, host_can):
        interactions = GAN[guest_can]["interactions"]
        for interaction, gan in interactions.items():
            if host_can == gan:
                return interaction
        return None

    @staticmethod
    def is_hop(guest_can, host_can):
        return "Tương hợp" == GanUtil.find_interaction(guest_can, host_can)

    @staticmethod
    def is_khac(guest_can, host_can):
        return "Tương khắc" == GanUtil.find_interaction(guest_can, host_can)

    @staticmethod
    def is_xung(guest_can, host_can):
        return "Tương xung" == GanUtil.find_interaction(guest_can, host_can)

    @staticmethod
    def is_same_polarity(guest_can, host_can):
        return GAN[guest_can]['polarity'] == GAN[host_can]['polarity']

    @staticmethod
    def get_polarity(can):
        return GAN[can]['polarity']

    @staticmethod
    def get_elemental(can):
        return GAN[can]['element']
