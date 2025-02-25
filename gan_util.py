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
