import subprocess


class TransmissionWrapper:

    def __init__(self):
        self.STATUS_CMD = 'transmission-remote -l'
        self.ADD_TORRENT = 'transmission-remote -a'
        self.REMOVE_TORRENT = 'transmission-remote -t'
        self.REMOVE_TORRENT = lambda t: 'transmission-remote -t ' + str(t) + ' --remove'
        self.PAUSE_TORRENT = lambda t: 'transmission-remote -t ' + str(t) + ' --stop'
        self.START_TORRENT = lambda t: 'transmission-remote -t ' + str(t) + ' --start'

    def torrents_status(self):
        raw_info = subprocess.check_output(self.STATUS_CMD.split())
        info = raw_info.decode().splitlines()
        info.pop(0)
        info.pop(-1)
        info_list = []
        for entry in info:
            entry_info = entry.split()
            print(entry_info)
            info_list.append({
                'target': entry_info[0],
                'pourcentage': entry_info[1],
                'size': entry_info[2],
                'size_unit': entry_info[3],
                'remaining_time': entry_info[4],
                'remaining_time_unit': entry_info[5],
                'upload_speed': entry_info[6],
                'download_speed': entry_info[7],
                'ratio': entry_info[8],
                'title': ''.join(entry_info[9:])
                })
        print(info_list)
        return info_list

    def add_torrent(self, magnet):
        cmd = self.ADD_TORRENT + ' ' + magnet
        res = subprocess.check_output(cmd.split())
        return res

    def remove_torrent(self, target):
        cmd = self.REMOVE_TORRENT(target)
        res = subprocess.check_output(cmd.split())
        return res

    def start_torrent(self, target):
        cmd = self.START_TORRENT(target)
        res = subprocess.check_output(cmd.split())
        return res

    def stop_torrent(self, target):
        cmd = self.PAUSE_TORRENT(target)
        res = subprocess.check_output(cmd.split())
        return res
