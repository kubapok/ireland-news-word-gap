from tqdm import tqdm
from transformers import pipeline

def get_formatted(text):
    answers = unmasker(text, top_k=15)
    answers = {x['token_str']:x['score'] for x in answers}
    empty = 1 - sum(answers.values())
    answers[''] = empty
    answers_str =''
    for k,v in answers.items():
        answers_str += k.strip()+':'+str(v) + ' '
    return answers_str.rstrip(' ').lstrip(' ')
    
def write(f_path_in, f_path_out):
    with open(f_path_in) as f_in, open(f_path_out,'w') as f_out:
        next(f_in)
        for line in tqdm(f_in,total=150_000):
            l_in = line.rstrip()
            a = get_formatted(l_in)
            f_out.write(a + '\n')

model = 'robertamodel/checkpoint-24000'
unmasker = pipeline('fill-mask', model=model)
write('dev-0_in.csv', '../dev-0/out.tsv')
write('test-A_in.csv', '../test-A/out.tsv')
