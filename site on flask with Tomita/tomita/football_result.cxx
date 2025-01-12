#encoding "utf-8"    // сообщаем парсеру о том, в какой кодировке написана грамматика
#GRAMMAR_ROOT S      // указываем корневой нетерминал грамматики
National -> Noun<gram="geo"> | Noun<c-agr[1]> Noun<gram="geo", c-agr[1]>;
Club -> Noun<h-reg1, quoted>;
Club -> Word<h-reg1, l-quoted> Word* Word<r-quoted>;
Team -> Club | National;

Name -> AnyWord<gram="persn", h-reg1, ~h-reg2>;
FO -> AnyWord<h-reg1, ~h-reg2, gram=~"geo, abbr", wfm="[A-ЯЁа-яё]{2,100}">;
FO -> UnknownPOS<h-reg1, ~h-reg2, gram=~"geo, abbr", wfm="[A-ЯЁа-яё]{2,100}">;
ABR -> Word<wfm="[A-Я.]{2}">;
ProperName ->  Name FO FO | FO FO Name | Name FO | FO Name | ABR+ FO | FO | FO ABR+;

Result -> Verb<kwtype="result_verb"> interp(ResultFact.Result::norm="nom,sg");
Score -> AnyWord<wff=/[0-9][:][0-9]/> interp(ResultFact.Score);
Score -> AnyWord<wff=/[0-9][-][0-9]/> interp(ResultFact.Score);
S -> Team interp(ResultFact.FirstTeam) AnyWord* Result AnyWord* Team interp(ResultFact.SecondTeam) AnyWord* Score;
S -> Team interp(ResultFact.FirstTeam) AnyWord* Team interp(ResultFact.SecondTeam) AnyWord* Result AnyWord* Score;
S -> Team interp(ResultFact.FirstTeam) AnyWord* Team interp(ResultFact.SecondTeam) AnyWord* Score;
S -> AnyWord<kwtype="goal_verb"> ProperName interp(GoalFact.Name) Punct ProperName interp(GoalFact.Name) SimConjAnd ProperName interp(GoalFact.Name);
S -> AnyWord<kwtype="goal_verb"> AnyWord* ProperName interp(GoalFact.Name);
Time -> AnyWord<gnc-agr[1]> "минута"<gnc-agr[1]>;
S -> Time interp(GoalFact.Time::norm="nom,sg,f") AnyWord* AnyWord<kwtype="goal_verb"> AnyWord* ProperName interp(GoalFact.Name);