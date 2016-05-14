import subprocess


class TransmissionWrapper:

    STATUS_CMD = 'transmission-remote -l'
    ADD_TORRENT = 'transmission-remote -a'
    REMOVE_TORRENT = 'transmission-remote --remove -t'

    def torrents_status(self):
        raw_info = subprocess.call(STATUS_CMD.split())
        info = raw_info.splitlines()
        info.pop(0)
        info.pop(1)
        info_list = []
        for entry in info:
            entry_info = entry.split()
            info_list.append({
                'target': entry_info[0],
                'pourcentage': entry_info[1],
                'size': entry_info[2],
                'size_unit': entry_info[3],
                'status': entry_info[4],
                'seeding_speed': entry_info[5],
                'download_speed': entry_info[6],
                'ratio': entry_info[7],
                'title': entry_info[8]
                })
        return info_list

    def add_torrent(self, magnet):
        cmd = ADD_TORRENT + ' ' + magnet
        res = subprocess.call(cmd.split())
        return res

    def remove_torrent(self, target):
        cmd = REMOVE_TORRENT + ' ' + target
        res = subprocess.call(cmd.split())
        return res
