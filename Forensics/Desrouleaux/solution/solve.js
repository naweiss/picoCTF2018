const obj = {
    "tickets": [
        {
            "ticket_id": 0,
            "timestamp": "2016/06/15 22:14:34",
            "file_hash": "7620d14475494d40",
            "src_ip": "234.9.10.90",
            "dst_ip": "176.71.176.149"
        },
        {
            "ticket_id": 1,
            "timestamp": "2017/01/15 16:23:55",
            "file_hash": "e290c6abb4a99e63",
            "src_ip": "234.9.10.90",
            "dst_ip": "214.68.112.230"
        },
        {
            "ticket_id": 2,
            "timestamp": "2015/08/27 23:19:00",
            "file_hash": "7620d14475494d40",
            "src_ip": "8.173.68.36",
            "dst_ip": "137.212.9.159"
        },
        {
            "ticket_id": 3,
            "timestamp": "2017/08/30 19:40:35",
            "file_hash": "baccdadc47af79f4",
            "src_ip": "62.191.39.220",
            "dst_ip": "123.2.252.7"
        },
        {
            "ticket_id": 4,
            "timestamp": "2017/02/03 16:51:58",
            "file_hash": "baccdadc47af79f4",
            "src_ip": "8.173.68.36",
            "dst_ip": "137.212.9.159"
        },
        {
            "ticket_id": 5,
            "timestamp": "2017/02/13 15:48:15",
            "file_hash": "7620d14475494d40",
            "src_ip": "62.191.39.220",
            "dst_ip": "214.68.112.230"
        },
        {
            "ticket_id": 6,
            "timestamp": "2016/11/12 17:54:40",
            "file_hash": "a36cb1580707d497",
            "src_ip": "32.42.74.225",
            "dst_ip": "137.212.9.159"
        },
        {
            "ticket_id": 7,
            "timestamp": "2017/06/05 00:29:26",
            "file_hash": "7638d9c4e75f2960",
            "src_ip": "53.213.218.12",
            "dst_ip": "184.90.119.16"
        },
        {
            "ticket_id": 8,
            "timestamp": "2016/01/03 14:41:29",
            "file_hash": "8ea38a0d8fa37077",
            "src_ip": "234.9.10.90",
            "dst_ip": "214.225.228.109"
        },
        {
            "ticket_id": 9,
            "timestamp": "2015/11/20 14:14:55",
            "file_hash": "e290c6abb4a99e63",
            "src_ip": "234.9.10.90",
            "dst_ip": "184.90.119.16"
        }
    ]
};

const src_ip_counts = Object.create(null);
obj.tickets.forEach(data => {
  src_ip_counts[data.src_ip] = src_ip_counts[data.src_ip] ? src_ip_counts[data.src_ip] + 1 : 1;
});

const keys = Object.keys(src_ip_counts);
const max_val =  Math.max.apply(null, keys.map(key => src_ip_counts[key]));
const max_src_ip = keys.filter(key => src_ip_counts[key] == max_val)[0];
console.log(`Most conmon source IP: ${max_src_ip}`);

const IP = prompt("Enter the requested IP");
const dst_ips = obj.tickets.filter(data => data.src_ip == IP);
const counts = Object.create(null);
dst_ips.forEach(data => {
  counts[data.dst_ip] = counts[data.dst_ip] ? counts[data.dst_ip] + 1 : 1;
});
console.log(`Unique destination IPs: ${Object.keys(counts).length}`);

const hashes = Object.create(null);
obj.tickets.forEach(data => {
  hashes[data.file_hash] = {};
});

Object.keys(hashes).forEach(hash => {
  obj.tickets.forEach(data => {
	  if (data.file_hash == hash)
		hashes[hash][data.dst_ip] = 1;
  });
});

const total_unique_ips = Object.keys(hashes)
	.reduce((acc, hash) => acc + Object.keys(hashes[hash]).length, 0);
const avg_uniqe_ips_per_hash = total_unique_ips / Object.keys(hashes).length;

console.log(`Average unique IPs per hash: ${avg_uniqe_ips_per_hash}`);